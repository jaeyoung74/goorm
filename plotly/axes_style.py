# update_xaxes(), update_yaxes() - 각각 X축, Y축에 관한 다양한 편집이 가능
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

#Axes Title - 축 스타일 설정방법
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


#Axes Title - 축 타이틀 위치 지정 방법
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


#축 타이틀 삭제방법
import plotly.express as px
#데이터 불러오기
df = px.data.tips()
#그래프 그리기
fig = px.scatter(df, x="total_bill", y="tip")
#축 레이블 삭제하기
fig.update_xaxes(title=None)
fig.update_yaxes(title=None)
fig.show()


#축 범위 지정하기
import plotly.express as px
#데이터 불러오기
df = px.data.iris()
#Figure 생성
fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
#축 범위 지정
fig.update_xaxes(range=[0, 5])
fig.update_yaxes(range=[0, 10])
fig.show()


#축 범위 역방향으로 지정하기
import plotly.express as px
#데이터 불러오기
df = px.data.iris()
#Figure 생성
fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
#y축 reverse
fig.update_yaxes(autorange="reversed")
fig.show()


#Log 스케일 지정하기
import plotly.graph_objects as go
import numpy as np

#데이터 생성
x = np.linspace(1, 200, 30)
#Figure 생성
fig = go.Figure(go.Scatter(x=x, y=x**3))
#축 Log 스케일로 변환
fig.update_xaxes(type="log")
fig.update_yaxes(type="log")
fig.show()