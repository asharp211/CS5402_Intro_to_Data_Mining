# Anthony Sharp
# AVSRCM
# 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

df = pd.read_csv('census.csv')

missing_Val = '?'
# Length of Row
_lenRow = df.index.size
_lenCol = len(df.columns)

_female = ['f','F','female', 'fem',' Female']
_male = ['m', 'M', 'male', 'mail',' Male']

#print(_len)
print(df)

# Question 1 part 1
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%m/%d/%Y")

for d in range(_lenRow):
    # Q1 part 2
    df["date"][d] =re.sub('/[0-9][0-9]*[0-9][0-9]','/1994', df["date"][d])
    # Question 3
    df["workclass"][d]= df["workclass"][d].replace(missing_Val, 'Other')
    # Question 5
    df["occupation"][d]= df["occupation"][d].replace(missing_Val, 'Other')
    # Question 6
    for i in range(5):
        if (df["sex"][d] == _female[i]):
            df["sex"][d]= df["sex"][d].replace(_female[i], 'Female')
        elif (df["sex"][d] == _male[i]):
            df["sex"][d]= df["sex"][d].replace(_male[i], 'Male')
        else:
            continue
    # Question 8
    df["native-country"][d]= df["native-country"][d].replace(missing_Val, 'Unspecified')


# Question 2
from sklearn.preprocessing import KBinsDiscretizer
from feature_engine.discretisers import EqualWidthDiscretiser as EWD

discretizer = EWD(bins=10,variables=['age'])
df = discretizer.fit_transform(df)

_X = df.iloc[:,1].values.reshape(-1,1)
plt.hist(_X, 10)
plt.show()

# Question 4
max_value = df["population-wgt"].max()
min_value = df["population-wgt"].min()
df["population-wgt"] = (df["population-wgt"]-min_value)/(max_value - min_value)

# Question 7
discretizer = EWD(bins=5,variables=["hours-per-week"])
df = discretizer.fit_transform(df)

HPW = df.iloc[:,1].values.reshape(-1,1)
plt.hist(HPW, 5)
plt.show()

# Question 9
from scipy.stats import chi2_contingency
from scipy.stats import chi2

#hold = []
split_df = ['age','workclass','education','marital-status','occupation',
            'relationship','race','sex','hours-per-week','native-country']

# Reflect, change the row to col
df1_T = df.T
# for i in range(len(split_df)):
#     for j in range(i+1, len(split_df)):
#         print(split_df[i]+ '  X  '+ split_df[j])


#chi2 =  sum {(o -exp)^2/exp}
# 
# 
# #


#newDF = df[split_df]
#_lenCol = len(newDF.columns)
#chi, pval, dof, exp = chi2_contingency(newDF)
#print(pd.DataFrame(
#    data=exp[:,:],
#    index=['age','workclass'],
#    columns=['workclass','education']).round(2))


#significance = 0.05
#p = 1 - significance
#crit_Val = chi2.ppf(p, dof)

#print('chi=%.6f, critical value=%.6f\n' % (chi, crit_Val))
#if chi > crit_Val:
#    print("""At %.2f level of significance, we reject the null hypotheses and accept H1.They are not independent.""" % (significance))
#else:
#    print("""At %.2f level of significance, we accept the null hypotheses. They are independent.""" % (significance))

# Question 10


# Question 11

df.to_csv("census1.csv", index=False)