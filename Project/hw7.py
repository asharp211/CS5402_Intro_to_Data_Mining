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
atribute_list = list(df.columns)
print(atribute_list)

_lenRow = df.index.size

_lenCol = len(df.columns)

_no = ['n','N','NO','No']
_yes = ['y','Y','YES','Yes']
_bad = ['b','B','Bad','BAD']
_good = ['g','G','Good','GOOD']

df['application_date'] = pd.to_datetime(df['application_date']).dt.strftime("%m/%d/%Y")

for i in range(_lenRow):
    #print(df['age'][i])
    if(df['age'][i] == missing_value):
        continue
    else:
        hold_val = df['age'][i]
        hold_val = abs(int(hold_val))
        df['age'][i] = hold_val
''' 
for k in attributeList:
    for i in range(_lenRow):
        for j in range(4):
            if(k == "foreign_worker" or k == "works_outside_US"):
                #print("stop Here")
                if(df[k][i] == _no[j]):
                    #print(df[k][i])
                    df[k][i] = df[k][i].replace(_no[j], 'no')
                elif(df[k][i] == _yes[j]):
                    df[k][i] = df[k][i].replace(_yes[j],'yes')
            elif(df[k][i] == _bad[j]):
                df[k][i] = df[k][i].replace(_bad[j],'Bad')
            elif(df[k][i] == _good[j]):
                df[k][i] = df[k][i].replace(_good[j],'Good')
            elif(df[k][i] == missing_value):
                df[k][i] = df[k][i].replace(_good[j],'Unknown')
            else:
                continue
        if(df[k][i] == missing_value):
            df[k][i] = df[k][i].replace(missing_value,'Unknown')

'''
for i in range(4):
    print(_no[i])
    df[atribute_list[21]] = df[atribute_list[21]].replace([_no[i]],'no')
    df[atribute_list[21]] = df[atribute_list[21]].replace([_yes[i]],'yes')
    df[atribute_list[22]] = df[atribute_list[22]].replace([_bad[i]],'Bad')
    df[atribute_list[22]] = df[atribute_list[22]].replace([_good[i]],'Good')
    df[atribute_list[25]] = df[atribute_list[25]].replace([_no[i]],'no')
    df[atribute_list[25]] = df[atribute_list[25]].replace([_yes[i]],'yes')

df[atribute_list[21]] = df[atribute_list[21]].replace(['1'],'Unknown')
df[atribute_list[21]] = df[atribute_list[21]].replace(['?'],'Unknown')
df[atribute_list[22]] = df[atribute_list[22]].replace(['?'],'Good')
df[atribute_list[25]] = df[atribute_list[25]].replace('1','Unknown')
df[atribute_list[25]] = df[atribute_list[25]].replace(missing_value,'Unknown')


df.to_csv("credit1.csv", index=False)