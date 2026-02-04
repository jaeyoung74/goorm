
#add_trace()
#figure에 새로운 trace 추가하기
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.show()


#이미 Trace가 있는 Figure에 Trace 추가해서 겹쳐 그리기
#이미 생성된 scatterplot 위에 직선의 그래프를 add_trace()를 활용해서 추가
import plotly.express as px
#데이터 불러오기
df = px.data.iris() 
#express를 활용한 scatter_plot 생성
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", 
                 title="Using The add_trace() method With A Plotly Express Figure")
#직선 그래프 추가
fig.add_trace(
    go.Scatter(
        x=[2, 4],
        y=[4, 8],
        mode="lines",
        line=go.scatter.Line(color="gray"),
        showlegend=False
    )
)
fig.show()

#update_traces(업데이트 내용)
#이미 생성된 trace의 type, 색, 스타일, 템플릿 등 추가 편집이 가능
import plotly.graph_objects as go
#그래프 생성
fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
#타이틀 추가하기
fig.update_layout(title_text="Using update_layout() With Graph object Figures", title_font_size=30)
fig.show()


#update_xaxes(), update_yaxes() - 각각 X축, Y축에 관한 다양한 편집이 가능
import plotly.graph_objects as go
import plotly.express as px
#데이터 생성
df = px.data.tips()
x = df["total_bill"]
y = df["tip"]
#그래프 그리기
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
#축 타이틀 추가하기
fig.update_xaxes(title_text="Totla Bill ($)")
fig.update_yaxes(title_text="Tip ($)")
fig.show()

