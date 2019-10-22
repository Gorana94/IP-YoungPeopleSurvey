import pandas as pd
df = pd.read_csv("responses.csv")
df
df.isnull().sum()

df_out1 = df = df.select_dtypes(include=['float64','int64']).apply(lambda x: x.fillna(x.mean().round(0)))
df_out1

df.isnull().sum()
df[df<5] = 0
df = df.replace(5.0, 1.0)
df = df.replace(4.0, 1.0)
df.insert(0,'id',range(0, len(df)))
df
df.to_csv('out.csv')