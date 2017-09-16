import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.DataFrame()
df_merge = pd.read_csv('../../data/merge.csv')

df['ID'] = df_merge['場次'].astype(str) + df_merge['部門'].astype(str)
df['species'] = df_merge['母品種']
df['times'] = df_merge['胎次']
df['birth_to_success'] = df_merge['母出生到配種成功']
df['breed_to_success'] = df_merge['初配種到成功']
df['success_to_live'] = df_merge['配種成功到分娩']
df['small_to_big'] = df_merge['分娩到斷乳']
df['score'] = df_merge['活著的平均重'] * df_merge['活幾頭']

df = df[df['species'].notnull()]
df = df[df['times'].notnull()]
df = df[df['birth_to_success'].notnull()]
df = df[df['birth_to_success'] > 0]
df = df[df['breed_to_success'].notnull()]
df = df[df['success_to_live'].notnull()]
df = df[df['small_to_big'].notnull()]
df = df[df['score'].notnull()]

le = preprocessing.LabelEncoder()
le.fit(df['species'])
le_species = le.classes_
df['species'] = le.transform(df['species'])

le.fit(df['ID'])
le_ID = le.classes_
df['ID'] = le.transform(df['ID'])

trainY = df['score'].tolist()
a1, a2, a3 = np.percentile(trainY, 25), np.mean(trainY), np.percentile(trainY, 75)
tmp = []
for i in trainY:
    if i <= a1:
        tmp.append(1)
    elif i >= a1 and i <= a2:
        tmp.append(2)
    elif i >= a2 and i <= a3:
        tmp.append(3)
    elif i >= a3:
        tmp.append(4)


X = np.asarray(df)
y = np.asarray(tmp)

final_score = 0
for i in range(0, 10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf = svm.SVC(C=2.0)
    clf.fit(X_train, y_train)
    predict = clf.predict(X_test)
    final_score += accuracy_score(y_test, predict)
    print(accuracy_score(y_test, predict))

print(final_score/10)
df.to_csv('test', index=False)
