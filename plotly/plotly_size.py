#plolty 그래프 사이즈 설정하기

#express 그래프
import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2], width=600, height=400)
fig.show()

#graph_object 그래프
import plotly.graph_objects as go
fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])])
fig.update_layout(width=500, height=400)
fig.show()

#margin 적용
import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
#그래프 크기와 margin 설정하기
fig.update_layout(
    width=600,
    height=400,
    margin_l=50,
    margin_r=50,
    margin_b=100,
    margin_t=100,
    #백그라운드 칼라 지정, margin 잘 보이게 하기위함
    paper_bgcolor="LightSteelBlue"
)
fig.show()