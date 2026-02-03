import pandas as pd

winedata = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/practice/winedata.csv")
print(winedata)

#요약함수
#describe() : 해당 컬럼 속성에 대한 고수준 요약 정보를 생성
#데이터 타입을 인식하기 때문에 입력 데이터의 타입에 따라 출력 결과가 달라짐
print(winedata.points.describe())
print(winedata.country.describe())

#mean() : 평균 점수 확인
print(winedata.points.mean())

#unique() : 고유한 값들의 목록
print(winedata.country.unique())

#value_counts() : 고유한 값들과 각각이 데이터셋에서 몇 번 등장하는지
print(winedata.country.value_counts())