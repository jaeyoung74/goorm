#그룹화계산
import pandas as pd
import numpy as np

idx=['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'E', 'E']
col = ['col1', 'col2', 'col3']
data = np.random.randint(0,9,(15,3))
df = pd.DataFrame(data=data, index=idx, columns=col).reset_index()

#index 컬럼에 대해서 groupby 수행
print(df.groupby('index'))

#groupby에 연산 메서드 추가
print(df.groupby('index').mean())
print(df.groupby('index').count())
print(df.groupby('index').agg(['sum', 'mean']))

#그룹화 계산
def top (df, n=2, col='col1'):
    return df.sort_values(by=col)[-n:] #상위 n개 열을 반환하는 함수 top 생성

print(df.groupby('index').apply(top))
print(df.groupby('index', group_keys=False).apply(top))

#observed 인수의 사용
df_cat = pd.Categorical(df['index'], categories=['A','B','C','D','E','F'])
print(df_cat)

print(df['col1'].groupby(df_cat).count())
print(df['col1'].groupby(df_cat,observed=True).count())

#as_index 인수의 사용
print(df.groupby(['index'], as_index=False).sum())

#dropna인수의 사용
df.loc[6,'index'] = np.nan
print(df)

print(df.groupby('index').sum())
print(df.groupby('index', dropna=False).sum())

#level인수의 사용
idx = [['idx1', 'idx1', 'idx2', 'idx2', 'idx2'], ['row1', 'row2', 'row1', 'row2', 'row3']]
col = ['col1', 'col2', 'col2']
data = np.random.randint(0,9,(5,3))
df = pd.DataFrame(data=data, index=idx, columns=col).rename_axis(index=['lv0', 'lv1'])
print(df)

print(df.groupby(level=1).sum())

print(df.groupby(['lv1','lv0']).sum())