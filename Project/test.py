from numpy import mean
from numpy import std
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.ensemble import GradientBoostingClassifier
from matplotlib import pyplot

df = pd.read_csv('credit.csv')

missing_value = '?'

#print(df.columns)
#print(df.columns == 'foreign_worker')
c = df.columns


#print(df[c[0]][0])

_lenRow = df.index.size
_lenCol = len(df.columns)

_no = ['n','N','0','NO','No']
_yes = ['y','Y','1','YES','Yes']
_bad = ['b','B','Bad','BAD', 'null']
_good = ['g','G','Good','GOOD', 'null']
#print(df["foreign_worker"])
#df.columns == 'foreign_worker' and df.columns == 'class' and df.columns == 'works_outside_US')

for i in range(_lenRow):
    if (df['state'][i] == missing_value):
        print(i)

for k in c:
    for i in range(_lenRow):
        #print(i)
        for j in range(5):
            #print(j)
            if(k == "foreign_worker" or k == "works_outside_US"):
                #print("stop Here")
                if(df[k][i] == _no[j]):
                    #print(df[k][i])
                    df[k][i] = df[k][i].replace(_no[j], 'no')
                elif(df[k][i] == _yes[j]):
                    df[k][i] = df[k][i].replace(_yes[j],'yes')
            elif(df[k][i] == _bad[j]):
                df[k][i] = df[k][i].replace(_bad[j],'bad')
            elif(df[k][i] == _good[j]):
                df[k][i] = df[k][i].replace(_good[j],'good')
            else:
                continue
df.to_csv("credit1.csv", index=False)