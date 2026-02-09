# b_team.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

#페이지 넓게 쓰기
st.set_page_config(layout="wide")

#사용할 시도 목록
PROVINCES = [
    "경기", "서울", "인천", "경북", "경남", "대구", "충남", "부산", "충북", "전북",
    "강원", "광주", "전남", "대전", "울산", "제주", "세종"
]

#CSV 로드 + 전처리
df = pd.read_csv("시군구별_월별_확진자_사망_발생현황_통합.csv")
df["날짜"] = pd.to_datetime(df["날짜"])

#시군구,확진자만
df = (
    df[df["유형"] == "확진자"]  #확진자만 
        .groupby(["날짜", "시도명"], as_index=False)["값"].sum() #시군구 합쳐서 시도별 합계
        .pivot(index="날짜", columns="시도명", values="값")
        .reset_index()
        .rename(columns={"날짜":"date"})
)

#date 타입 보정
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

#df에 실제 존재하는 지역만
regions_all = [r for r in PROVINCES if r in df.columns]

#컬럼타입
df[regions_all] = df[regions_all].apply(pd.to_numeric, errors="coerce").fillna(0)

def run_market_map_slider(df, selected_regions):
    
    df = df.copy()

    #날짜 처리/정렬
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    #선택 지역만 사용
    regions = [r for r in selected_regions if r in df.columns]

    #쓸 지역이 하나도 없으면 None 반환하고 끝
    if not regions:
        return None 

    # 숫자 변환
    df[regions] = df[regions].apply(pd.to_numeric, errors="coerce").fillna(0)

    #누적합
    df_cum = df.copy()
    df_cum[regions] = df_cum[regions].cumsum()
    
    #날짜 -> 리스트로
    dates = df_cum["date"].dt.strftime("%Y-%m-%d").tolist()

    labels = regions
    parents = [""] * len(regions)

    # 프레임 생성(날짜별)
    frames = []
    for i, d in enumerate(dates):
        row = df_cum.iloc[i]
        values = [row[r] for r in regions]

        frames.append(
            go.Frame(
                name=d,
                data=[go.Treemap(
                    labels=labels,
                    parents=parents,
                    values=values,
                    marker=dict(
                        colors=values,
                        colorscale="Reds",
                        line=dict(width=2)
                    ),
                    textfont=dict(size=18),
                    textinfo="label+value",
                    hovertemplate="<b>%{label}</b><br>누적값: %{value:,}<extra></extra>",
                )],
                layout=go.Layout(
                    title_text=f"마켓맵 (기준일: {d})"
                )
            )
        )

    # 초기 화면
    init_row = df_cum.iloc[0]
    init_values = [init_row[r] for r in regions]

    fig = go.Figure(
        data=[go.Treemap(
            labels=labels,
            parents=parents,
            values=init_values,
            marker=dict(
                colors=init_values,
                colorscale="Reds",
                line=dict(width=2)
            ),
            textfont=dict(size=18),
            textinfo="label+value",
            hovertemplate="<b>%{label}</b><br>누적값: %{value:,}<extra></extra>",
        )],
        frames=frames
    )

    # 슬라이더
    steps = []
    for d in dates:
        steps.append(dict(
            method="animate",
            args=[[d], {
                "mode": "immediate",
                "frame": {"duration": 0, "redraw": True},
                "transition": {"duration": 0}
            }],
            label=""
        ))

    fig.update_layout(
        height=700,
        margin=dict(t=120, l=10, r=10, b=140),

        updatemenus=[dict(
            type="buttons",
            direction="left",
            showactive=False,
            x=0.0,
            y=1.25,
            xanchor="left",
            yanchor="top",
            buttons=[
                dict(
                    label="▶ 재생",
                    method="animate",
                    args=[None, {
                        "frame": {"duration": 300, "redraw": True},
                        "transition": {"duration": 0},
                        "fromcurrent": True,
                        "mode": "immediate"
                    }]
                ),
                dict(
                    label="⏸ 정지",
                    method="animate",
                    args=[[None], {
                        "frame": {"duration": 0, "redraw": False},
                        "mode": "immediate"
                    }]
                ),
            ]
    )],

    sliders=[dict(
            active=0,
            x=0.05,
            len=0.90,
            y=0.0,
            yanchor="bottom",
            pad={"t": 10, "b": 0},
            currentvalue={"prefix": "기준일: "},
            steps=steps
        )],
    )

    return fig


#사이드바
with st.sidebar:
    st.title("🎛️ 컨트롤 패널")

    st.subheader("📅 분석 기간 설정")
    min_date = df["date"].min().date()
    max_date = df["date"].max().date()

    start_date, end_date = st.date_input(
        "날짜 범위 선택",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    st.markdown("---")

    st.subheader("🗺️ 관심 지역 선택")
    selected_regions = st.multiselect(
        "지역을 선택하세요 (기본: 전체)",
        regions_all,
        default=regions_all
    )

#데이터 필터링
mask = (df["date"] >= pd.to_datetime(start_date)) & (df["date"] <= pd.to_datetime(end_date))
filtered_df = df.loc[mask]

if filtered_df.empty or not selected_regions:
    st.warning("선택한 기간/지역에 해당하는 데이터가 없습니다. 다시 선택해주세요.")
else:
    fig = run_market_map_slider(filtered_df, selected_regions)
    if fig is None:
        st.warning("그래프를 만들 지역이 없습니다.")
    else:
        st.plotly_chart(fig, use_container_width=True)
