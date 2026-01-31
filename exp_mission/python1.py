#리스트와 딕셔너리 사용하기
data1 = [1,2,3,'apple',[1,3,4]]
print(data1)

print(data1[1:2])
print(data1[3])

data1.append(4)
print(data1)

data1.append("tree")
print(data1)

data1.remove("tree")
print(data1)

data1.remove(data1[2])
print(data1)

#리스트 컴프리헨션 사용하기
numbers = [x for x in range(10)]
print(numbers)

numbers1 = [2 * x for x in range(1, 10+1)]
print(numbers1)

numbers2 = [x for x in range(1, 10+1) if x % 2 == 0]
print(numbers2)

menu = [ (x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']]
[('쌈밥', '사과'),
 ('쌈밥', '아이스크림'),
 ('쌈밥', '커피'),
 ('치킨', '사과'),
 ('치킨', '아이스크림'),
 ('치킨', '커피'),
 ('피자', '사과'),
 ('피자', '아이스크림'),
 ('피자', '커피')]

print(menu)

#문자열 다루기 연습
str = "string"
print(str[0])
print(str[0:4])
print(str.upper())

str1 = "STRING"
print(str1.lower())

#문자열 포매팅 연습
name = "홍길동"
age = 25
job = "학생"

print(f"이름은 {name}이고, 나이는 {age}살이며, 직업은 {job}입니다.")
