#pandas 라이브러리 불러오기
import pandas as pd

#DataFrame
df1 = pd.DataFrame({'Yes':[50, 21], 'No':[131, 2]})
print(df1)

df2 = pd.DataFrame({'Bob':['I liked it.', 'It was awful.'], 'Sue':['Pretty good.', 'Bland.']})
print(df2)

df3 = pd.DataFrame({'Bob':['I liked it.', 'It was awful.'], 'Sue':['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])
print(df3)

#Series
sr1 = pd.Series([1, 2, 3, 4, 5])
print(sr1)

sr2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(sr2)

#실제 데이터 불러오기
game_data = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/practice/games.csv")

#데이터 크기
print("데이터 크기: ", game_data.shape)

#데이터 미리보기
print(game_data.head())

#인덱스 지정하기
game_data = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/practice/games.csv", index_col=0)
print(game_data.head())
