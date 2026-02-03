#graph_objects 패키지를 go로 불러옴
import plotly.graph_objects as go

#go.Figure() 함수를 활용해서 기본 그래프를 생성
#figure는 plotly 작업의 기본 단위/ go.Figure() 함수를 통해 생성 가능
fig = go.Figure(
    #Data 입력
    data = [go.Bar(x=[1,2,3], y=[1,3,2])],
    #layout 입력
    layout=go.Layout(
        title=go.layout.Title(text="A Figure Specified By A Graph Object")
    )
)
#show 하면 내 노트북(주피터 노트북)에 그래프가 나타남
fig.show()