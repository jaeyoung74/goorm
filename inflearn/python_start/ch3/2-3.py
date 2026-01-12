# 파이썬 변수

#기본 선언
n = 700

#출력
print(n)
print(type(n)) #n의 타입 출력

#동시 선언 가능
x = y = z = 700
print(x, y, z)

#선언
var = 75

#재선언
var = "Change Value"

#출력
print(var)
print(type(var))

#id 확인 : 객체의 고유값 확인
m = 800
n = 600

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

#같은 오브젝트 참조
m =800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))

#다양한 변수 선언
#Camel Case -> Method
numberOfCollegeGraduates = 1

#Pascal Case -> Class
NumberOfColleageGraduates = 1

#Snake Case 
number_of_college_graduates = 1