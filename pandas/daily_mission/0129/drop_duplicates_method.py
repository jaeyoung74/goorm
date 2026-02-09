#drop_duplicates
#내용이 중복되는 행을 제거하는 메서드
#df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_indes=False)
#subset : 중복값을 검사할 열/ 기본적으로 모든 열을 검사
#keep : {first/last} 중복제거를 할 때 남길 행/ first면 첫 값을 남기고 last면 마지막 값을 남김
#inplace : 원본을 변경할지의 여부임
#ignore_index : 원래 index를 무시할 지 여부

import pandas as pd

game = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/0129/games.csv")
df = pd.DataFrame(game)
print(df)

#subset에 입력된 컬럼명을 기준으로 해당 컬럼의 중복값을 검사하게 됨
#따로 입력되지 않는 경우는 모든 열에 대해 값이 중복인 행을 제거함
print(df.drop_duplicates())

#subset에 특정 컬럼명만 입력할 경우, 해당 열에 대해서만 중복값 검사를 수행
print(df.drop_duplicates(subset='id'))

#keep인수
#중복값을 제거하고 남길 행을 선택할 수 있음
#keep='first'인 경우 처음 값을 남김
print(df.drop_duplicates(subset='id', keep='first'))
#keep='last'인 경우 마지막 값을 남김
print(df.drop_duplicates(subset='id', keep='last'))

#ignore_index=True
print(df.drop_duplicates(subset='id', keep='last', ignore_index=True))