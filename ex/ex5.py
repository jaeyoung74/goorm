#딕셔너리 자료형
#1
d = {"a":1, "b":2}
print(d['a'])

#2
d = {"a":1}
d["b"] = 2
print(d)

#3
d = {"a":1, "b":2}
print(d.keys())

#4
d = {"a":1, "b":2}
print(d.values())

#5
d = {"a":1, "b":2}
print(d.get('c',0))

#6
d = {"apple":3, "banana":5}
d["apple"] = 10
print(d)

#7
d = {"a":1, "b":2}
del d["a"]
print(d)

#8
d = {"apple":3, "banana":5}
for k,v in d.items():
    print(k,v)

#9
l = [("a", 1), ("b", 2)]
print(dict(l))

#10
d = {"a":1, "b":2, "c":3}
print(sum(d.values()))