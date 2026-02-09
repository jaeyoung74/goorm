# insert 메소드 구현하기
import pandas as pd

game = pd.read_csv("/Users/goorm/desktop/goorm/python_start/pandas/daily_mission/0129/games.csv")

#insert: 열삽입
#-> DataFrame의 특정 위치에 열을 삽입하는 메서드
#해당 열이 이미 존재할 경우 allow_duplicates=True가 아니면 Value Errer를 발생시킴

#loc: 몇번째 열에 집어넣을지
#column: 열 이름
#value: 값
#allow_duplicates: default값이 False고 True로 하면 열이름 중복해서 사용가능
df = pd.DataFrame(game)
print(df)

df.insert(1, "name", "Young")
print(df)

df.insert(2, "num", 10, allow_duplicates=False)
print(df)