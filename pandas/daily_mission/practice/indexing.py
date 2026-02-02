import pandas as pd

wine_data = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/practice/winedata.csv")
print(wine_data.head())

#특정 Series(열) 선택하는 방법
#1
print(wine_data.country)
#2
print(wine_data['country'])

#특정 하나의 값 접근하기
print(wine_data['country'][1])


#iloc : 인덱스 기반 선택
#시작 포함 / 끝 제외
#행출력
print(wine_data.iloc[2])
#열출력
print(wine_data.iloc[:,1])
#처음 3개 행의 country 열만 선택
print(wine_data.iloc[:3,1])
#2,3번째 행의 country 열만 선택
print(wine_data.iloc[1:3,1])
#리스트를 전달
print(wine_data.iloc[[0,1,2],1])
#음수 인덱스도 사용가능
print(wine_data.iloc[-5:])


#loc : 라벨 기반 선택
#시작 포함 / 끝 포함
print(wine_data.loc[:, ['country', 'variety', 'winery']])

#인덱스는 고정된 것이 아니라 변경 가능
print(wine_data.set_index("country"))

#조건 기반 질문
#와인이 이탈리아산인지 확인
print(wine_data.country == 'Italy')

#위 결과를 loc 안에서 사용해 필요한 데이터만 선택가능
#이탈리아산인 와인만 출력
print(wine_data.loc[wine_data.country=='Italy'])

#이탈리아산 & 90점이상
print(wine_data.loc[(wine_data.country=='Italy') & (wine_data.points >= 90)])

#이탈리아산 | 90점이상
print(wine_data.loc[(wine_data.country=='Italy') | (wine_data.points >= 90)])


#isin
#값이 리스트 안에 포함되어 있는지
#이탈리아산,프랑스산 와인만 선택
print(wine_data.loc[wine_data.country.isin(['Italy', 'France'])])

#isnull, notnull
#값이 비어있는지 여부를 확인
#가격 정보가 없는 와인은 제외
print(wine_data.loc[wine_data.price.notnull()])

#값을 할당하기
wine_data['critic']='everyone'
print(wine_data['critic'])

wine_data['index_backwards'] = range(len(wine_data), 0, -1)
print(wine_data['index_backwards'])

