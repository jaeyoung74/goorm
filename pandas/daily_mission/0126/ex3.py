import pandas as pd

data1 = pd.read_csv("daily_mission/0126/WA_Fn-UseC_-HR-Employee-Attrition.csv")

print(data1.head())

print(data1.loc[1:10])
print(data1.loc[:"Age"])
print(data1.iloc[0])
print(data1.iloc[1:3])
print(data1.iloc[:0:3])

#조건부조회
print(data1["Age"] >= 50)

#수정
data1['Age']=30
print(data1.head())

#삭제
data1.drop(["Age"],axis=1)
print(data1.head())

#합계
sum1 = data1.sum(axis=0)
print(sum1)

#나누기
data1['Age'].divide(2)
print(data1.head())
