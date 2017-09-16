import pandas as pd

df_stat = pd.DataFrame()
df = pd.read_csv('../../data/merge.csv')
df['ID'] = df['場次'].astype(str) + df['部門'].astype(str)
ID_all = df['ID'].tolist()
ID = list(set(ID_all))

count, a, b, live, die = [], [], [], [], []
for i in ID:
    count.append(ID_all.count(i))
    a.append(i)
    b.append(df.loc[df['ID'] == i, '生幾頭'].sum())
    live.append(df.loc[df['ID'] == i, '活幾頭'].sum())
    die.append(df.loc[df['ID'] == i, '死幾頭'].sum())

df_stat['ID'] = pd.Series(a).values
df_stat['count'] = pd.Series(count).values
df_stat['平均一胎總數'] = pd.Series(b).values / df_stat['count']
df_stat['平均一胎活著數'] = pd.Series(live).values / df_stat['count']
df_stat['平均一胎死亡數'] = pd.Series(die).values / df_stat['count']

df_stat.to_csv('../../data/about_place_in_merge', index=False)
