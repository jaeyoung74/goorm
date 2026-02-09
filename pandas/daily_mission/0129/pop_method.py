# pop 메소드 구현하기
import pandas as pd

game = pd.read_csv("/Users/goorm/desktop/goorm/python_start/pandas/daily_mission/0129/games.csv")

#pop: DataFrame에서 열 레이블을 꺼냄
#즉, 원본 DataFrame에서 해당 열이 제거됨
#df.pop(item)
#item: 꺼낼 열의 이름
df = pd.DataFrame(game)
print(df.head())

item = df.pop('rated')
print(item)
print(df.head())

