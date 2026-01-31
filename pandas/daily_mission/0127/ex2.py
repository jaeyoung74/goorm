#지수가중함수 (ewm)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numba

data = {'val':[1,4,2,3,2,5,13,10,12,14,np.nan,16,12,20,22]}
df = pd.DataFrame(data).reset_index()
print(df)

df2 = df.assign(ewm=df['val'].ewm(alpha=0.3).mean())
ax = df.plot(kind='bar', x='index', y='val')
ax2 = df2.plot(kind='line', x='index', y='ewm', color='red', ax=ax)
print(plt.show())

df2 = df.assign(dwm_a_low=df['val'].ewm(alpha=0.1).mean())
df3 = df.assign(ewm_a_high=df['val'].ewm(alpha=0.7).mean())
ax = df.plot(kinds='bar', x='index', y='val')
ax2 = df2.plot(kind='line', x='index', y='ewm_a_low', color='red', ax=ax)
ax3 = df3.plot(kind='line', x='index', y='ewm_a_high', color='green', ax=ax)
print(plt.show())

df2 = df.assign(span_4=df['val'].ewm(span=4).mean())
df3 = df.assign(span_8=df['val'].ewm(span=8).mean())
ax = df.plot(kine='bar', x='index', y='val')
ax2 = df2.plot(kind='line', x='index', y='span_4', color='red', ax=ax)
ax3 = df3.plot(kind='line', x='index', y='span_8', color='green', ax=ax)
print(plt.show())

df2 = df.assign(com_2=df['val'].ewm(com=2).mean())
df3 = df.assign(com_10=df['val'].ewm(com=10).mean())
ax = df.plot(kind='bar', x='index', y='val')
ax2 = df2.plot(kind='line', x='index', y='com_2', color='red', ax=ax)
ax3 = df3.plot(kind='line', x='index', y='com_10', color='green', ax=ax)
print(plt.show())

df2 = df.assign(harf_2=df['val'].ewm(halflife=2).mean())
df3 = df.assign(harf_5=df['val'].ewm(halflife=5).mean())
ax = df.plot(kind='bar', x='index', y='val')
ax2 = df2.plot(kind='line', x='index', y='harf_2', color='red', ax=ax)
ax3 = df3.plot(kind='line', x='index', y='harf_5', color='green', ax=ax)
print(plt.show())

df2 = df.assign(adj_True=df['val'].ewm(alpha=0.2,adjust=True).mean())
df3 = df.assign(adj_False=df['val'].ewm(alpha=0.2, adjust=False).mean())
ax = df.plot(kind='bar', x='index', y='val')
ax2 = df2.plot(kind='line', x='index', y='adj_True', color='red', ax=ax)
ax3 = df3.plot(kind='line', x='index', y='adj_False', color='green', ax=ax)
print(plt.show())

df2 = df.assign(ignore_na_True=df['val'].ewm(alpha=0.2, ignore_na=True).mean())
df3 = df.assign(ignore_na_False=df['val'].ewm(alpha=0.2, ignore_na=False).mean())
ax = df.plot(kind='bar', x='index', y='val')
ax2 = df2.plot(kind='line', x='index', y='ignore_na_True', color='red', ax=ax)
ax3 = df3.plot(kind='line', x='index', y='ignore_na_False', color='green', ax=ax)
print(plt.show())

#numba
print(df['val'].ewm(alpha=0.2, method='table').mean(engine='numba'))