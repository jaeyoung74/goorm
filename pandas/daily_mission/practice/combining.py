import pandas as pd

#combining : 결합하기

#concat() : 리스트 형태로 전달된 객체들을 지정한 축을 기준으로 그대로 이어붙임
#같은 컬럼 구조를 가진 여러 DataFrame이나 Series가 서로 다른 객체로 나뉘어 있을 때 특히 유용

#YouTube Videos 데이터셋은 국가별로 파일이 나뉘어져 있음. concat()으로 합치기
c_youtube = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/practice/CAvideos.csv")
d_youtube = pd.read_csv("/Users/goorm/Desktop/goorm/python_start/pandas/daily_mission/practice/DEvideos.csv")
print(pd.concat([c_youtube, d_youtube]))

#join() : 공통된 인덱스를 가진 DataFrame들을 결합할 때 사용
#같은 날에 트렌딩된 동일한 영상을 찾아 결합하기
left = c_youtube.set_index(['title', 'trending_date'])
right = d_youtube.set_index(['title', 'trending_date'])
print(left.join(right, lsuffix='_CAN', rsuffix='_UK'))