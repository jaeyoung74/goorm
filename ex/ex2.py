#문자열 자료형
#1번
s = "python hi"
print(len(s))

#2번
s = "hello world"
print(s[0])
print(s[-1])

#3번
s = "hello python"
print(s.upper())

#4번
s = "HELLO WORLD"
print(s.lower())

#5번
s = "I like apples"
print(s.count('a'))

#6번
s = "hello"
print(s[::-1])
'''
    s[시작위치:끝위치:이동방향]
     -> 이동방향이 +1 이면 왼에서 오
        이동방향이 -1 이면 오에서 왼
'''

#7번
s = "hello python"
if s.find('python') > 0:
    print("true")
else:
    print("false") 

#8번
s = "hello world"
print(s.replace(" ",""))

#9번
s = "abdd"
if s == s[::-1]:
    print(True)
else:
    print(False)  

#10번
s = "abc123"
answer = ""
for i in s:
    if i.isdigit():
        answer += i

print(answer)
  