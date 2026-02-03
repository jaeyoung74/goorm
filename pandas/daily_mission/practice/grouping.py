import pandas as pd

winedata = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/practice/winedata.csv")

#그룹 단위 분석
#groupby()
#같은 점수를 받은 리뷰들을 하나의 그룹으로 묶음
#그다음 각 그룹에 대해 points 컬럼을 선택하고 해당 값이 몇 번 등장하는지를 계산함
print(winedata.groupby('points').points.count())

#그룹화된 데이터에도 모든 요약 함수를 적용할 수 있음
#점수별로 가장 저렴한 와인을 구하기
print(winedata.groupby('points').price.min())
#각 그룹은 조건에 맞는 데이터만 포함하는 DataFrame의 일부라고 생각할 수 있음
#DataFrame은 apply() 메서드를 통해 직접 접근할 수 있으며 원하는 방식으로 자유롭게 조작가능

#데이터셋에서 각 와이너리별로 가장 먼저 리뷰된 와인의 지역을 선택하는 방법
print(winedata.groupby('winery').apply(lambda df: df.country.iloc[0]))

#여러 컬럼으로 그룹화하기
#국가와 주 별로 가장 높은 점수를 받은 와인을 선택하기
print(winedata.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))

#agg메서드 : 여러함수를 동시에 적용할 수 있게 해줌
#국가별로 가격 데이터에 대한 간단한 통계 요약만들기
print(winedata.groupby(['country']).price.agg([len, min, max]))

#다중메서드 : 하나의 인덱스가 여러 단계를 가짐
countries_reviewed = winedata.groupby(['country', 'province']).description.agg([len])
print(countries_reviewed)

mi = countries_reviewed.index
print(type(mi))

#reset_index() : 다중 인덱스에서 일반 인덱스로 되돌리기
print(countries_reviewed.reset_index())