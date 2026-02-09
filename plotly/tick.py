#tick(눈금) 기본 생성 및 위치 지정
import plotly.express as px
#데이터 불러오기
df = px.data.iris()
#Figure 생성
fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
#눈금 생성
fig.update_xaxes(ticks="outside")
fig.update_yaxes(ticks="inside")
fig.show()

#그래프 1개만 선택해서 눈금 추가하기
import plotly.express as px
#데이터 불러오기
df = px.data.iris()
#Figure 생성
fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
#눈금 생성
fig.update_xaxes(ticks="outside")
fig.update_yaxes(ticks="inside", col=1)
fig.show()


#눈금 간격 지정
import plotly.express as px
#데이터 불러오기
df = px.data.iris()
#Figure 생성
fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
#눈금 생성 + 눈금 간격 지정
fig.update_xaxes(ticks="outside", dtick=0.5)
fig.update_yaxes(ticks="inside", dtick=2)
fig.show()


#눈금 위치 수동 입력
import plotly.express as px
#데이터 불러오기
df = px.data.iris()
#Figure 생성
fig = px.scatter(df, "sepal_width", y="sepal_length", facet_col="species")
#눈금 생성 + 눈금 위치 수동 입력
fig.update_yaxes(tickvals=[5.1, 5.9, 6.3, 7.5])
fig.show()


