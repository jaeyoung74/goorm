#concat 메서드 구현하기
import pandas as pd

s1 = pd.Series(["a", "b"])
s2 = pd.Series(["c", "d"])

print(pd.concat([s1, s2]))
print(pd.concat([s1, s2], ignore_index=True))
print(pd.concat([s1, s2], keys=["s1", "s2"]))
print(pd.concat([s1, s2], keys=["s1", "s2"], names=["Series name", "Row ID"]))

df1 = pd.DataFrame([["a", 1], ["b", 2]], columns=["letter", "number"])
print(df1)

df2 = pd.DataFrame([["c", 3], ["d", 4]], columns=["letter", "number"])
print(df2)

print(pd.concat([df1, df2]))



game = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/0129/games.csv")
cavideos = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/0129/games.csv")

df3 = pd.DataFrame(game)
df4 = pd.DataFrame(cavideos)

print(pd.concat([df3, df4]))
