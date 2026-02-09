import pandas as pd
import plotly.graph_objects as go
import streamlit as st

def build_vaccine_dashboard(df: pd.DataFrame):
    """
    3조 통합용:
    - app.py에서 전달받은 df로만 그래프 생성
    - 파일 내부에서 CSV를 읽지 않음
    - fig.show() 대신 fig 반환
    """

    # 필요한 컬럼 체크
    need = ["date", "death", "accumulated_vaccine_count"]
    missing = [c for c in need if c not in df.columns]
    if missing:
        # Streamlit에서 메시지 보고 싶으면 st.error 사용
        st.error(f"백신 그래프에 필요한 컬럼이 없습니다: {missing}")
        return None

    d = df.copy()
    d["date"] = pd.to_datetime(d["date"])

    # (예시) 누적접종(선) vs 일일사망(막대) 이중축
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=d["date"],
            y=d["death"],
            name="일일 사망자",
            opacity=0.4
        )
    )

    fig.add_trace(
        go.Scatter(
            x=d["date"],
            y=d["accumulated_vaccine_count"],
            name="누적 백신 접종",
            mode="lines",
            yaxis="y2"
        )
    )

    fig.update_layout(
        title="백신 접종(선)과 사망자(막대) 변화",
        xaxis=dict(title="날짜"),
        yaxis=dict(title="일일 사망자 수"),
        yaxis2=dict(title="누적 접종 수", overlaying="y", side="right"),
        hovermode="x unified",
        template="plotly_white",
        height=500
    )

    return fig
