#drop 메소드 구현하기

#drop
#DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
#drop 메서드: 데이터프레임에서 열을 삭제하는 메서드/ pop과 다르게 원본이 변경되지 않음
import pandas as pd

game = pd.read_csv("/Users/goorm/desktop/goorm/python_start/pandas/daily_mission/0129/games.csv")

deep = game.copy(deep=True)
shallow = game.copy(deep=False)
print(game)

df = pd.DataFrame(game)
print(df.drop(labels = 1, axis=0))
print(df.drop(labels='id', axis=1))

#index인수와 columns인수로 삭제
#index 사용헤서 삭제
print(df.drop(index=1))
#columns 사용해서 삭제
print(df.drop(columns='id'))

#errors인수
#삭제하고자하는 렐이블이 존재하지 않으면 오류가 발생함
#errors='ignore' 로 설정하면 오류를 발생하지 않음

#오류빌셍
#print(df.drop(labels=[20058, 20059], errors='raise'))
#errors='ignore'사용
print(df.drop(labels=[20058, 20059], errors='ignore'))


#inpalce인수로 원본 변경
df.drop(labels=['id'], axis=1, inplace=True)
print(df)