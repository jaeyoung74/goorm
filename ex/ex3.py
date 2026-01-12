#리스트 자료형

#1
l = [1,2,3,4,5]
print(sum(l))

#2
l = [1,2,3,4,5]
a = []
for i in l:
    if i % 2 == 0:
        a.append(i)
print(a)  

#3
l = [3,1,4,2]
l.sort()
print(l)

#4
l = [10, 20, 30, 40]
print(max(l))

#5
l = [10, 20, 30, 40]
print(min(l))

#6
l = [1,2,3,4,5]
l.reverse()
print(l)

#7
l = [1,2,3,2,2,4]
print(l.count(2))

#8
l = [1,2,3]
l.append(4)
print(l)

#9
l = [1,2,3,4,5]
print(l[1:4])

#10
l = [1,2,3,4,5]
a = []
for i in l:
    a.append(str(i))
print(a)

