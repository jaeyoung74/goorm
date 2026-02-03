import pandas as pd

winedata = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/practice/winedata.csv")
print(winedata)

#map : 하나의 값 집합을 다른 값 집합으로 매핑하는 함수를 의미함

#map()
#전달하는 함수는 Series의 단일 값 하나를 입력으로 받아 변환된 값을 반환해야 함
#모든 값이 해당 함수로 변환된 새로운 Series를 반환함 
#와인점수를 평균이 0이 되도록 조정하기
winedata_points_mean = winedata.points.mean()
print("map() : ",winedata.points.map(lambda p: p - winedata_points_mean))

#apply() : 각 행에 사용자 정의 함수를 적용하여 DataFrame 전체를 변환하고 싶을 때 사용하는 메서드
#winedata.apply()를 axis='index'로 호출했다면, 각 행이 아니라 각 컬럼을 변환하는 함수를 전달해야 함
def remean_points(row):
    row.points = row.points - winedata_points_mean
    return row

print("apply() : ", winedata.apply(remean_points, axis='columns'))

#map()과 apply()는 새로운 변환된 Series나 DataFrame을 반환하며 원본 데이터 자체르 수정하지는 않음
print("원본데이터",winedata.head(1))

#백터화 연산
#점수 컬럼의 평균을 빼는 작업
winedata_points_mean = winedata.points.mean()
print("벡터화 연산", winedata.points - winedata_points_mean)

#길이가 같은 Series끼리의 연산도 처리 가능
#국가와 지역 정보를 하나로 결합하기
print(winedata.country + " - " + winedata.region_1)