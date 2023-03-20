import statsmodels.api as sm
from statsmodels.stats.proportion import proportion_confint
#import numexpr as ne
import pandas as pd
import numpy as np
#import csv

df = pd.read_csv("breast-cancer.csv")
f = open("rules_in_List.txt","r+")

#    int  int float , int int float, int int float
# [[[4, 4, 'yes'], [5, 4, '1']], [[9, 4, 'recurrence-events']]]
outer_row_list = []
for row in df:
    outer_row_list.append(row)

print(df.loc[df["tumor-size"] == '0-4',:])
print(df.loc[df["age"] == '40-49',:])