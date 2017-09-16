import pandas as pd
import numpy as np

df_f = pd.DataFrame()
df = pd.DataFrame()

df_id = pd.read_csv('../../data/identification_pruned.csv')
df_birth = pd.read_csv('../../data/birth_pruned.csv')

girl_id = df_birth['母ID'].tolist()
boy_id = df_birth['公ID'].tolist()
all_id = df_id['ID'].tolist()
species = df_id['品種'].tolist()
birth = df_id['出生日期'].tolist()
count = 0
g_species, g_birth = [], []
for i in girl_id:
    if i in all_id:
        j = all_id.index(i)
        g_species.append(species[j])
        g_birth.append(birth[j])
    else:
        count += 1
        g_species.append(None)
        g_birth.append(None)
print(count)
count = 0
b_species, b_birth = [], []
for i in boy_id:
    i = i.split('|')[:-1]
    i = ''.join(i)
    if i in all_id:
        j = all_id.index(i)
        b_species.append(species[j])
        b_birth.append(birth[j])
    else:
        count += 1
        b_species.append(None)
        b_birth.append(None)
print(count)
df_birth['分娩日期'] = pd.to_datetime(df_birth['分娩日期'], errors='coerce')
df_birth['母豬離乳日期'] = pd.to_datetime(df_birth['母豬離乳日期'], errors='coerce')
df_birth['初配日期'] = pd.to_datetime(df_birth['初配日期'], errors='coerce')
df_birth['受孕日期'] = pd.to_datetime(df_birth['受孕日期'], errors='coerce')
df_birth['母出生日期'] = pd.to_datetime(pd.Series(g_birth).values, errors='coerce')
df_birth['公出生日期'] = pd.to_datetime(pd.Series(b_birth).values, errors='coerce')


df['A'], df_f['場次'], df_f['部門'], df_f['耳號'], df_f['年期'] = \
    df_birth['母ID'].str.split('|').str
df_f['胎次'] = df_birth['胎次']
df_f['生幾頭'] = df_birth['分娩活仔數']
df_f['死幾頭'] = df_birth['死亡仔數']
df_f['活幾頭'] = df_birth['斷乳仔數']
df_f['活著的平均重'] = df_birth['平均活仔重']
df_f['活著的平均重'] = df_f['活著的平均重'].replace(np.inf, 0)
df_f['母品種'] = pd.Series(g_species).values
df_f['公品種'] = pd.Series(b_species).values
df_f['母出生到配種成功'] = df_birth['受孕日期'].sub(df_birth['母出生日期'], axis=0)
df_f['母出生到配種成功'] = df_f['母出生到配種成功'] / np.timedelta64(1, 'D')
df_f['公出生到配種成功'] = df_birth['受孕日期'].sub(df_birth['公出生日期'], axis=0)
df_f['公出生到配種成功'] = df_f['公出生到配種成功'] / np.timedelta64(1, 'D')
df_f['初配種到成功'] = df_birth['受孕日期'].sub(df_birth['初配日期'], axis=0)
df_f['初配種到成功'] = df_f['初配種到成功'] / np.timedelta64(1, 'D')
df_f['配種成功到分娩'] = df_birth['分娩日期'].sub(df_birth['受孕日期'], axis=0)
df_f['配種成功到分娩'] = df_f['配種成功到分娩'] / np.timedelta64(1, 'D')
df_f['分娩到斷乳'] = df_birth['母豬離乳日期'].sub(df_birth['分娩日期'], axis=0)
df_f['分娩到斷乳'] = df_f['分娩到斷乳'] / np.timedelta64(1, 'D')

df_f.to_csv('../../data/merge.csv', index=False)
