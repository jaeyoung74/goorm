import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")

df = pd.read_csv("cleaned_covid_data.csv")

#date 컬럼을 날짜 타입으로 변환
df["date"] = pd.to_datetime(df["date"])

#사용할 시도 목록
PROVINCES = [
    "경기", "서울", "인천", "경북", "경남", "대구", "충남", "부산", "충북", "전북",
    "강원", "광주", "전남", "대전", "울산", "제주", "세종"
]

#df.columns에서 찾기
available_provinces = [p for p in PROVINCES if p in df.columns]

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
        available_provinces,
        default=available_provinces
    )

    #데이터 필터링
    mask = (df["date"] >= pd.to_datetime(start_date)) & (df["date"] <= pd.to_datetime(end_date))
    filtered_df = df.loc[mask]

#기간 내 지역별 확진자 합계
agg_df = (
    filtered_df[selected_regions]
    .sum()
    .reset_index()
    .rename(columns={"index": "region", 0: "cases"})
)

#그래프
if agg_df.empty:
    st.warning("선택한 기간/지역에 해당하는 데이터가 없습니다. 다시 선택해주세요.")
else:
    fig = go.Figure(
        data = go.Bar(
            x=agg_df["region"],
            y=agg_df["cases"],
            text=agg_df["cases"],
            textposition="outside",
            marker=dict(color="#4CAF50")
        )
    )

    fig.update_layout(
        title=f"지역별 신규 확진자 ({start_date} ~ {end_date})",
        xaxis_title="지역",
        yaxis_title="확진자 수", 
        height=700
    )

    st.plotly_chart(fig, use_container_width=True)

