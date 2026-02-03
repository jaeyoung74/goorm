import pandas as pd

winedata = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/practice/winedata.csv")

#renaming : 인덱스 이름이나 컬럼 이름을 변경할 수 있음
#데이터셋에서 points 컬럼을 score로 바꾸기
winedata = winedata.rename(columns={'points':'score'})
print(winedata.score)

#인덱스의 일부 값 변경
winedata = winedata.rename(index={0: 'firstEntry', 1: 'secondEntry'})
print(winedata.head())

#rename_axis() : 인덱스 이름과 컬럼 이름 변경
#행 인덱스에는 wines, 컬럼 인덱스에는 fields
winedata = winedata.rename_axis("wines", axis="rows").rename_axis("fields", axis="columns")
print(winedata.head())
