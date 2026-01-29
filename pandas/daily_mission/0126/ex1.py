import pandas as pd

nums = [i for i in range(1,11)]
print(nums)

#series 데이터 설정방법
SeriesNums = pd.Series(nums)
print(SeriesNums)

#평균값 출력
print(SeriesNums.mean())

#분석값 출력
print(SeriesNums.describe())

#DataFrame 생성방법
nums1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

dfNums1 = pd.DataFrame(nums1)
print(dfNums1)
print(dfNums1[0])

nums2 = pd.DataFrame({'Yes':[50,21], 'No':[131,2]})
print(nums2)

nums3 = pd.DataFrame({'Bob':['I liked it.', 'It was awful.'], 'Sue':['Pretty good.', 'Bland.']})
print(nums3)

#데이터파일 불러오기
wine_reviews = pd.read_csv("daily_mission/0126/winemag-data-130k-v2.csv")

print(wine_reviews.shape)
print(wine_reviews.head())

wine_reviews1 = pd.read_csv("daily_mission/0126/winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews1.head())