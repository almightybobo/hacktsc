#!/usr/bin/python3
# -*- coding: utf-8 -*- i
import pandas as pd
df_br = pd.read_csv('../../data/raw_utf8/birth.csv', sep = ',')
df_br = df_br.loc[:,['場號', '部門', '耳號', '年期', '胎次', '配種公豬耳號', \
                     '公豬年期', '分娩活仔數', '死亡仔數', '斷乳仔數', \
                     '斷乳窩重', '分娩日期', '母豬離乳日期', '初配日期', '受孕日期']]
df_br['耳號'] = df_br['耳號'].astype(str).str.replace('.0', '')
df_br['耳號'] = df_br['耳號'].str.rjust(7,'0')
df_br['配種公豬耳號'] = df_br['配種公豬耳號'].astype(str).str.replace('.0', '')
df_br['配種公豬耳號'] = df_br['配種公豬耳號'].str.rjust(7,'0')
# 去除死亡數異常的行位
df_br = df_br[df_br['分娩活仔數'] == (df_br['死亡仔數'] + df_br['斷乳仔數'])]
# 新增平均活仔重的欄位
df_br['平均活仔重'] = (df_br['斷乳窩重'] - df_br['死亡仔數'])/df_br['斷乳仔數']
# ID重製
df_br['母ID'] = '2|' + df_br['場號'].astype(str) + '|' + df_br['部門'].astype(str) + \
    '|' + df_br['耳號'].astype(str) + '|' + df_br['年期'].astype(str)
df_br['公ID'] = '1|' + df_br['場號'].astype(str) + '|' + df_br['部門'].astype(str) + \
    '|' + df_br['配種公豬耳號'].astype(str) + '|' + df_br['公豬年期'].astype(str)
# 除去冗餘欄位
df_br = df_br.drop(['場號', '部門', '耳號', '年期', '配種公豬耳號', '公豬年期'],\
    axis=1)
df_br.to_csv('../../data/birth_pruned.csv', index=False)
