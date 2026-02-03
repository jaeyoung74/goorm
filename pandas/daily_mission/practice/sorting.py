import pandas as pd

winedata = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/practice/winedata.csv")

#결과 행의 순서는 데이터 값이 아니라 인덱스 값에 의해 결정됨

#sort_values() : 원하는 순서로 데이터를 정렬하기 / 기본적으로 오름차순 정렬
countries_reviewed = winedata.groupby(['country', 'province']).description.agg([len])
countries_reviewed = countries_reviewed.reset_index()

#오름차순정렬
sort1 = countries_reviewed.sort_values(by='len')
print("sort1", sort1)

#내림차순정렬
sort2 = countries_reviewed.sort_values(by='len', ascending=False)
print("sort2", sort2)

#인덱스 값 기준으로 정렬하기
sort3 = countries_reviewed.sort_index()
print("sort3", sort3)

#여러 컬럼을 동시에 기준으로 정렬가능
sort4 = countries_reviewed.sort_values(by=['country', 'len'])
print(sort4)

