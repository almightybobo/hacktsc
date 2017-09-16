import pandas as pd

# 讀取資料集及生成新ID
df = pd.read_csv('data/raw_utf8/sales.csv')
df['ID']  = df['場號'].astype(str) + df['部門'].astype(str)

# 取出內銷資料，並增減欄位
df_type40 = df[df['銷售別'] == 40]
df_type40 = df_type40.loc[:, ['ID', '實售總頭數', '合計市場磅重', '實售總金額']]
df_type40['每磅平均金額'] = df_type40['實售總金額'] / df_type40['合計市場磅重']
df_type40['每隻平均磅數'] = df_type40['合計市場磅重'] / df_type40['實售總頭數']
#df_type40['9830']['每磅平均金額'] = df_type40['9830']['每磅平均金額']/756

df_dept = df_type40.groupby(['ID']).mean()
df_dept.to_csv('data/sales_each_dept.csv')
