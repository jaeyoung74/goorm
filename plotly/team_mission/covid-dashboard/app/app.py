import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path

from Cteam_vaccination_vs_severe_rate_correlation import build_vaccine_dashboard

# -----------------------------------------------------------------------------
# 페이지 설정
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="코로나19 종합 상황실",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# 커스텀 CSS
# -----------------------------------------------------------------------------
st.markdown(
    """
<style>
/* =========================
   Tabs
   ========================== */
.stTabs [data-baseweb="tab-list"] { gap: 10px; }
.stTabs [data-baseweb="tab"] {
  height: 60px;
  border-radius: 10px 10px 0 0;
  font-weight: bold;
  font-size: 1.1rem;
  border: none;
  transition: all 0.3s;
  padding: 0px 15px 0px 15px;
}

.stTabs [data-baseweb="tab"]:nth-of-type(1) { background-color: #E3F2FD; color: #1565C0; }
.stTabs [data-baseweb="tab"]:nth-of-type(1)[aria-selected="true"] {
  background-color: #2196F3; color: white; box-shadow: 0px -4px 10px rgba(33,150,243,0.3);
}

.stTabs [data-baseweb="tab"]:nth-of-type(2) { background-color: #E8F5E9; color: #2E7D32; }
.stTabs [data-baseweb="tab"]:nth-of-type(2)[aria-selected="true"] {
  background-color: #4CAF50; color: white; box-shadow: 0px -4px 10px rgba(76,175,80,0.3);
}

.stTabs [data-baseweb="tab"]:nth-of-type(3) { background-color: #FFF3E0; color: #EF6C00; }
.stTabs [data-baseweb="tab"]:nth-of-type(3)[aria-selected="true"] {
  background-color: #FF9800; color: white; box-shadow: 0px -4px 10px rgba(255,152,0,0.3);
}

.block-container { padding-top: 2rem; }

/* =========================
   Multiselect tag (선택된 지역 태그)
   ========================== */
.stMultiSelect [data-baseweb="tag"] {
  background-color: #E3F2FD;   /* 연한 블루 */
  color: #1565C0;
  border-radius: 8px;
  font-weight: 500;
  padding: 13px;
}

/* 태그 X 버튼 */
.stMultiSelect [data-baseweb="tag"] svg { fill: #1565C0; }

/* =========================
   Multiselect box (빨간 포커스 테두리 → 연한 파랑)
   ========================== */
.stMultiSelect [data-baseweb="select"] > div {
  border: 0px solid rgba(0,0,0,0.15) !important;
  box-shadow: none !important;
  padding: 8px 0 5px 8px !important;
}

.stMultiSelect [data-baseweb="select"] > div:focus-within {
  border: 1.5px solid #90CAF9 !important;
  box-shadow: 0 0 0 2px rgba(33,150,243,0.15) !important;
  outline: none !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 데이터 로드
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "data" / "cleaned_covid_data.csv"
    if not file_path.exists():
        return None
    df_ = pd.read_csv(file_path)
    df_["date"] = pd.to_datetime(df_["date"])
    return df_


df = load_data()
if df is None:
    st.error("🚨 데이터 파일이 없습니다! data/cleaned_covid_data.csv 위치를 확인하세요.")
    st.stop()

# -----------------------------------------------------------------------------
# 사이드바 필터
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("🎛️ 컨트롤 패널")

    st.subheader("📅 분석 기간 설정")
    min_date = df["date"].min()
    max_date = df["date"].max()

    date_range = st.date_input(
        "날짜 범위 선택",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    # Streamlit 반환값이 date 1개일 때도 안 터지게
    if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
        start_date, end_date = date_range
    elif isinstance(date_range, (list, tuple)) and len(date_range) == 1:
        start_date = end_date = date_range[0]
    else:
        start_date = end_date = date_range

    st.markdown("---")

    st.subheader("🗺️ 관심 지역 선택")
    exclude_cols = [
        "date",
        "total",
        "domestic",
        "overseas",
        "death",
        "daily_vaccine_count",
        "accumulated_vaccine_count",
    ]
    all_regions = [c for c in df.columns if c not in exclude_cols and "접종" not in c]

    selected_regions = st.multiselect(
        "지역을 선택하세요 (기본: 전체)",
        all_regions,
        default=all_regions,
    )

    st.info(f"📊 총 {len(df)}일간의 데이터를 분석합니다.")

# -----------------------------------------------------------------------------
# 기간 필터링
# -----------------------------------------------------------------------------
mask = (df["date"].dt.date >= start_date) & (df["date"].dt.date <= end_date)
filtered_df = df.loc[mask].copy()

# -----------------------------------------------------------------------------
# 메인
# -----------------------------------------------------------------------------
st.title("🦠 코로나19 데이터 분석 종합 대시보드")
st.markdown(f"**기간:** {start_date} ~ {end_date}")

if filtered_df.empty:
    st.warning("⚠️ 선택한 기간에 데이터가 없습니다. 날짜 범위를 넓혀주세요.")
    st.stop()

# KPI 값
total_cases = int(filtered_df["total"].sum())
total_deaths = int(filtered_df["death"].sum())
total_vax = (
    int(filtered_df.iloc[-1]["accumulated_vaccine_count"])
    if "accumulated_vaccine_count" in filtered_df.columns
    else 0
)

# 사망자 추이 (최근 7일 평균 vs 직전 7일 평균) - 데이터 짧으면 가능한 범위에서 비교
death_series = filtered_df["death"].astype(float)

if len(death_series) >= 14:
    last7 = death_series.tail(7).mean()
    prev7 = death_series.tail(14).head(7).mean()
elif len(death_series) >= 2:
    last_n = min(7, len(death_series))
    last7 = death_series.tail(last_n).mean()
    prev_part = death_series.head(max(1, len(death_series) - last_n))
    prev7 = prev_part.mean()
else:
    last7 = prev7 = float(death_series.iloc[0])

if last7 > prev7:
    death_delta_text = "사망자 증가(최근7일)"
    death_delta_color = "inverse"  # 빨강
elif last7 < prev7:
    death_delta_text = "사망자 감소(최근7일)"
    death_delta_color = "normal"  # 초록
else:
    death_delta_text = "변화 없음(최근7일)"
    death_delta_color = "off"

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("총 확진자 수", f"{total_cases:,}명")
with col2:
    st.metric("총 사망자 수", f"{total_deaths:,}명", delta=death_delta_text, delta_color=death_delta_color)
with col3:
    st.metric("누적 백신 접종", f"{total_vax:,}건")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["📈 2조: 종합 추이", "🗺️ 2조: 지역별 현황", "💉 2조: 백신 효과"])

# -----------------------------------------------------------------------------
# 탭1: 종합 추이
# -----------------------------------------------------------------------------
with tab1:
    st.subheader("📊 국내 코로나19 확진 및 사망 추이")

    fig_a = go.Figure()
    fig_a.add_trace(
        go.Scatter(
            x=filtered_df["date"],
            y=filtered_df["total"],
            name="신규 확진자",
            mode="lines",
            yaxis="y1",
        )
    )
    fig_a.add_trace(
        go.Scatter(
            x=filtered_df["date"],
            y=filtered_df["death"],
            name="신규 사망자",
            mode="lines",
            yaxis="y2",
        )
    )

    fig_a.update_layout(
        xaxis=dict(title="날짜"),
        yaxis=dict(title="확진자 수", side="left", showgrid=False),
        yaxis2=dict(title="사망자 수", overlaying="y", side="right", showgrid=False),
        template="plotly_white",
        hovermode="x unified",
        height=500,
        legend=dict(x=0.01, y=0.99),
    )
    st.plotly_chart(fig_a, use_container_width=True)

# -----------------------------------------------------------------------------
# 탭2: 지역별 현황 (필터 마지막 날짜 기준)
# -----------------------------------------------------------------------------
with tab2:
    st.subheader("🗺️ 지역별 확진자 발생 비교")

    if not selected_regions:
        st.warning("⚠️ 사이드바에서 지역을 하나 이상 선택해주세요.")
        st.stop()

    latest_row = filtered_df.iloc[-1]

    region_data = (
        pd.DataFrame(
            {"Region": selected_regions, "Count": [latest_row[r] for r in selected_regions]}
        )
        .sort_values("Count", ascending=False)
        .reset_index(drop=True)
    )

    fig_b = px.bar(
        region_data,
        x="Region",
        y="Count",
        color="Count",
        title=f"지역별 신규 확진자 ({latest_row['date'].date()} 기준)",
        text_auto=".2s",
        color_continuous_scale="Greens",
    )
    fig_b.update_layout(
        xaxis_title="지역",
        yaxis_title="확진자 수",
        template="plotly_white",
        height=500,
    )
    st.plotly_chart(fig_b, use_container_width=True)

# -----------------------------------------------------------------------------
# 탭3: 백신 효과 (2조 파일 함수 호출)
# -----------------------------------------------------------------------------
with tab3:
    st.subheader("💉 백신 접종과 사망률 변화 시각화")

    try:
        fig_c = build_vaccine_dashboard(filtered_df)
        st.plotly_chart(fig_c, use_container_width=True)
    except Exception as e:
        st.error(f"🚨 백신 그래프 생성 실패: {e}")
