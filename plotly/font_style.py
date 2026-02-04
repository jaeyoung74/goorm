#제목 폰트 스타일 지정
import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2], title="Title 설정하기")

fig.update_layout(
    #타이틀 위치 설정 부분
    title_y = 0.9,
    title_x = 0.5,
    title_xanchor = 'center',
    title_yanchor = 'middle',
    #폰트 스타일 추가 부분
    title_font_size = 25,
    title_font_color = "red", 
    title_font_family = "Times"
)
fig.show()


#축 타이틀 생성
import plotly.graph_objects as go
import plotly.express as px

#데이터 생성
df = px.data.tips()
x = df["total_bill"]
y = df["tip"]
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))

fig.update_xaxes(title_text='Total Bill ($)')
fig.update_yaxes(title_text='Tip ($)')

fig.show()

#축 타이틀명 변경
import plotly.express as px
#데이터 불러오기
df = px.data.tips()
#그래프 그리기
fig = px.scatter(df, x="total_bill", y="tip")
#축 타이틀 스타일 지정부분
fig.update_xaxes(title_text='Total Bill ($)',
                 title_font_size=30,
                 title_font_color='crimson',
                 title_font_family='Courier')
fig.update_yaxes(title_text='Tip ($)',
                 title_font_size=30,
                 title_font_color='crimson',
                 title_font_family='Courier')
fig.show()


#축 타이틀 위치 지정
import plotly.express as px
#데이터 불러오기
df = px.data.tips()
#그래프 그리기
fig = px.scatter(df, x="total_bill", y="tip")
#축 타이틀 스타일 + 위치 지정 부분
fig.update_xaxes(title_text='Total Bill ($)',
                 title_font_size=30,
                 title_font_color='crimson',
                 title_font_family='Courier',
                 title_standoff=100)
fig.update_yaxes(title_text='Tip ($)',
                 title_font_size=30,
                 title_font_color='crimson',
                 title_font_family='Courier',
                 title_standoff=100)
fig.show()