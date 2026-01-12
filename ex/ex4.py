#튜플 자료형
#1
t= (1,2,3,4)
print(len(t))

#2
t = (10, 20, 30)
print(t[0])

#3
t = (10, 20, 30)
print(list(t))

#4
t = (1,2,3)
a = (4,5)
t += a
print(t)

#5
t = (1,2,3,2,2)
print(t.count(2))

#6
t = (10, 20, 30)
a, b, c = t
print(a, b, c)

#7
t = (5,1,3)
print(sorted(t))

#8
t = (1,3,5,6,3,2,4)
print(4 in t)


#9
l = [1, 2, 3]
print(tuple(l))

#10
a = (1,2,3)
a[1] = 3


