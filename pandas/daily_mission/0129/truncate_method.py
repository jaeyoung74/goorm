#truncate 메소드
#행이나 열에 대해서 앞뒤를 자르는 메서드

import pandas as pd

game = pd.read_csv("/Users/goorm/desktop/goorm/python_start/pandas/daily_mission/0129/games.csv")
df = pd.DataFrame(game)

#행 자르기
print(df.truncate(before=1, after=2, axis=0))

#열 자르기
df1 = df.sort_index(axis=1)
print(df1.truncate(before='id', after='opening_ply', axis=1))