import pandas as pd
import numpy as np

df = pd.read_csv('../..//data/raw_utf8/identification.csv')
df_main = df[['場號', '部門', '耳號', '年期', '性別', '出生日期', '胎次', '母耳號', \
              '父耳號', '配種日期', '初配種日期', '分娩日期', '斷乳日期', '品種']]

DF = pd.DataFrame()
DF['ID'] = df['場號'].astype(str) + '|' + df['部門'].astype(str) + '|' \
              + df['耳號'].astype(str) + '|' + df['年期'].astype(str)

df_main['配種日期'] = pd.to_datetime(df_main['配種日期'], errors='coerce')
df_main['出生日期'] = pd.to_datetime(df_main['出生日期'], errors='coerce')
df_main['初配種日期'] = pd.to_datetime(df_main['初配種日期'], errors='coerce')
df_main['分娩日期'] = pd.to_datetime(df_main['分娩日期'], errors='coerce')
df_main['斷乳日期'] = pd.to_datetime(df_main['斷乳日期'], errors='coerce')

DF['出生到配種成功'] = df_main['配種日期'].sub(df_main['出生日期'], axis=0)
DF['出生到配種成功'] = DF['出生到配種成功'] / np.timedelta64(1, 'D')
DF['配種到成功'] = df_main['配種日期'].sub(df_main['初配種日期'], axis=0)
DF['配種到成功'] = DF['配種到成功'] / np.timedelta64(1, 'D')
DF['配種到分娩'] = df_main['分娩日期'].sub(df_main['配種日期'], axis=0)
DF['配種到分娩'] = DF['配種到分娩'] / np.timedelta64(1, 'D')
DF['分娩到斷乳'] = df_main['斷乳日期'].sub(df_main['分娩日期'], axis=0)
DF['分娩到斷乳'] = DF['分娩到斷乳'] / np.timedelta64(1, 'D')

DF = DF[DF['出生到配種成功'] > 0]
DF = DF[DF['配種到成功'] >= 0]
DF = DF[DF['配種到分娩'] > 0]
DF = DF[DF['分娩到斷乳'] > 0]

DF['胎次'] = df_main['胎次']
DF['母耳號'] = df_main['母耳號']
DF['父耳號'] = df_main['父耳號']
DF['品種'] = df_main['品種']
DF['出生日期'] = df_main['出生日期']

DF.to_csv('../../data/identification_pruned.csv', index=False)
