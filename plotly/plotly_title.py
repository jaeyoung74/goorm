#plotly 타이틀 설정하기 - express 그래프
import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2], title="Title 설정하기")
fig.show()

#plotly 타이틀 설정하기 - graph_object 그래프
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(x=[1, 2 ,3], y=[1, 3, 2])],
    layout=go.Layout(title=go.layout.Title(text="Title 설정하기"))
)
fig.show()


#update_layout()
#express 방법
import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.update_layout(title_text="타이틀 설정하기")
fig.show()

#graph_objects 방법
import plotly.graph_objects as go
fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])])
fig.update_layout(title_text="타이틀 설정하기")
fig.show()


#타이틀 위치 지정
import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2], title="Title 위치 설정하기")
#타이틀 위치 설정부분
fig.update_layout(
    title_x = 0.5, 
    title_y = 0.9,
    title_xanchor = "center",
    title_yanchor = "middle"
)
fig.show()


