import streamlit as st
import pandas as pd
import plotly.graph_objects as go
 

df = pd.read_csv("cleaned_covid_data.csv")
print(df.head())

#date 컬럼을 날짜 타입으로 변환
df["date"] = pd.to_datetime(df["날짜"])

#숫자 변환
df["cases_raw"] = pd.to_numeric(df["값"], errors="coerce").fillna(0)

#사용할 시도 목록
PROVINCES = [
    "경기", "서울", "인천", "경북", "경남", "대구", "충남", "부산", "충북", "전북",
    "강원", "광주", "전남", "대전", "울산", "제주", "세종"
]

#데이터에 실제 존재하는 시도만 추리기
available_provinces = [p for p in PROVINCES if p in df["sido"].unique()]


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

    # 참고 정보
    st.info(f"📊 총 {df['date'].nunique()}개 날짜(월) 데이터가 있습니다.")

    #데이터 필터링
    mask = (df["date"] >= pd.to_datetime(start_date)) & (df["date"] <= pd.to_datetime(end_date))
    filtered_df = df.loc[mask]

    filtered_df = filtered_df[filtered_df["sido"].isin(selected_regions)]

#도 기준으로 시군구 합치기
agg_df = (
    filtered_df
    .groupby("sido", as_index=False)["monthly_cases"]
    .sum()
    .rename(columns={"sido":"region", "monthly_cases":"cases"})
)


#그래프
if agg_df.empty:
    st.warning("선택한 기간/지역에 해당하는 데이터가 없습니다. 다시 선택해주세요.")
else:
    fig = go.bar(
        agg_df,
        x="region",
        y="cases",
        text="cases",
        title=f"지역별 신규 확진자({start_date} ~ {end_date})",
        labels={"region":"지역", "cases":"확진자수"}
    )

    st.plotly_chart(fig, use_container_width=True)

