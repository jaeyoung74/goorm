import pandas as pd

winedata = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/practice/winedata.csv")

#Dtypes (데이터 타입) : DataFrame이나 Series에서 각 컬럼이 가지는 데이터 타입
#문자열로만 이루어진 컬럼은 전용 문자열 타입을 가지지 않고 object 타입으로 저장됨
#특정 컬럼 dtype 확인
print(winedata.price.dtype)

#모든 컬럼 dtype 확인
print(winedata.dtypes)

#astype() : 데이터 타입 변환하기
#points 데이터 타입 int64 -> float64로 변환하기
print(winedata.points.astype('float64'))

#인덱스도 자체적인 dtype을 가짐
print(winedata.index.dtype)

#결측 데이터
#값이 없는 데이터는 NaN으로 표시됨
#NaN값은 항상 float64 타입을 가짐

#pd.isnull() , pd.notnull()
print(winedata[pd.isnull(winedata.country)])
print(winedata[pd.notnull(winedata.country)])

#fillna : 결측값 채우기
print(winedata.region_2.fillna('Unknown'))

#replace() : 값 바꾸기
print(winedata.country.replace("Italy", "korea"))