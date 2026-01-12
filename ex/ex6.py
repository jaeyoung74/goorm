#집합 자료형
#1
my_set = set([1,2,3,4,5])
print(my_set)

#2
nums = [1,2,2,3,3,3,4]
unique_nums = set(nums)
print(unique_nums)

#3
s = {1,2,3}
s.add(4)
print(set)

#4
s = {1,2}
s.update([3,4,5])
print(s)

#5
s = {1,2,3}
s.discard(5)
print(s)

#6
A = {1,2,3,4}
B = {3,4,5,6}
print(A&B)

#7
print(A|B)

#8
print(A-B)

#9
text = "Hello World"
print(len(set(text)))

#10
sub = {1,2}
main = {1,2,3,4}
print(sub.issubset(main)) #부분집합

