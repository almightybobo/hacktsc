#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas as pd

df_br = pd.read_csv('../../data/raw_utf8/birth.csv', sep = ',')

df_br = df_br.loc[:,['場號', '部門', '耳號', '年期', '胎次', '配種公豬耳號', \
                     '公豬年期', '分娩活仔數', '死亡仔數', '斷乳仔數', \
                     '斷乳窩重', '分娩日期', '母豬離乳日期']]
print(len(df_br))
