import pandas as pd

df1 = pd.DataFrame({"A":[1,2,3], "B":[10,20,30]})
df2 = pd.DataFrame({"A":[4,5,6], "B":[1,2,3]})

print("df1\n", df1)
print("df2\n", df2)

print("덧셈\n", df1+df2)
print()
print("뺄셈\n", df1-df2)
print()
print("곱셈\n", df1*df2)
print()
print("나눗셈\n", df1/df2)