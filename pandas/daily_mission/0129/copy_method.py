# copy 메소드 구현하기
#copy: pandas 객체를 복사함
#deep copy 와 shallow copy 기능을 지원함

#deep: {True or False} 기본값 True
#deep=True : deep copy/ 원본과는 완전하게 별개인 복사본이 생성됨/ 사본, 원본의 수정은 서로에게 영향을 끼치지 않음
#deep=False : shallow copy/ 원본의 데이터 및 인덱스를 복사하지 않고 새 객체를 호출함/ 원본 데이터가 수정되면 사본의 데이터도 수정되고 그 반대도 마찬가지.
import pandas as pd
game = pd.read_csv("/Users/goorm/desktop/goorm/python_start/pandas/daily_mission/0129/games.csv")
df = pd.DataFrame(game)

deep = df.copy(deep=True)
shallow = df.copy(deep=False)

print(df)

df[0] = "apple"
shallow[1] = 10
deep[1] = 7

print(df)
print(shallow)
print(deep)