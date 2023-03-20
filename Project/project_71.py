import numpy as np
import pandas as pd
import math
from scipy.stats import chi2_contingency
from scipy.stats import chi2
from scipy.stats import spearmanr
from sklearn.decomposition import PCA

df = pd.read_csv('credit.csv')

atribute_list = list(df.columns)
print(atribute_list)

print(df[atribute_list[0]].value_counts())

df[atribute_list[0]] = df[atribute_list[0]].replace(["?"],str("Los Angeles, CA"))
X = df[atribute_list[0]].copy()
print(df[atribute_list[0]].value_counts())
df[atribute_list[0]].value_counts().to_csv('location.csv')

df[atribute_list[1]] = df[atribute_list[1]].replace(["?"],"California")
print(df[atribute_list[1]].value_counts())

df[atribute_list[2]] = df[atribute_list[2]].replace(["?"],"0")

df[atribute_list[2]] = pd.to_numeric(df[atribute_list[2]])
print(df[atribute_list[2]].value_counts())

#print(df[atribute_list[3]])


#df[atribute_list[3]] = df[atribute_list[3]].astype(int)
#df.loc[df.duration<=10,"duration"] = 1
##df.loc[df[atribute_list[3]] = 10,:] = 1

df.loc[df[atribute_list[3]] == "?",atribute_list[3]] = 0

df[atribute_list[3]] = pd.to_numeric(df[atribute_list[3]])
MEAN = df.loc[df[atribute_list[3]] != 0,atribute_list[3]].mean()
MEAN = int(np.floor(MEAN))
df.loc[df[atribute_list[3]] == 0,atribute_list[3]] = MEAN

df[atribute_list[3]].to_csv("location.csv")

print(atribute_list[4])
print(df[atribute_list[4]])
df[atribute_list[4]] = df[atribute_list[4]].replace(["?"],str('no credit history'))
df[atribute_list[4]].value_counts().to_csv('credit_history')

print(atribute_list[5])

df[atribute_list[5]] = df[atribute_list[5]].replace(["?"],"Unknown")
df[atribute_list[5]].value_counts().to_csv('purpose')

df.loc[df[atribute_list[6]] == "?",atribute_list[6]] = 0
df[atribute_list[6]] = pd.to_numeric(df[atribute_list[6]])
MEAN = df.loc[df[atribute_list[6]] != 0, atribute_list[6]].mean()

df.loc[df[atribute_list[6]]==0,atribute_list[6]] = int(MEAN)

df[atribute_list[6]].value_counts().to_csv('creditamount')

df[atribute_list[7]] = df[atribute_list[7]].replace(["?"],'0')
df[atribute_list[7]] = pd.to_numeric(df[atribute_list[7]])

df[atribute_list[7]].value_counts().to_csv("saveings")

df[atribute_list[8]] = df[atribute_list[8]].replace(["?"],"Unknown")
df[atribute_list[8]].value_counts().to_csv("employ")

df[atribute_list[9]] = df[atribute_list[9]].replace(["?"],"0")
df[atribute_list[9]] = pd.to_numeric(df[atribute_list[9]])
df[atribute_list[9]].value_counts().to_csv("installment_commitment")

df[atribute_list[10]] = df[atribute_list[10]].replace(["?"],'Unknown')
df[atribute_list[10]].value_counts().to_csv("personal_status")

df[atribute_list[11]] = df[atribute_list[11]].replace(["?"],"Unknown")
df[atribute_list[11]].value_counts().to_csv("other_parties")

df[atribute_list[12]] = df[atribute_list[12]].replace(["?"],"0")
df[atribute_list[12]].value_counts().to_csv("residence_since")

df[atribute_list[13]] = df[atribute_list[13]].replace(["?"],"Other")
df[atribute_list[13]].value_counts().to_csv("property_magnitude")

df[atribute_list[14]] = df[atribute_list[14]].replace(["?"],'0')

df[atribute_list[14]] = pd.to_numeric(df[atribute_list[14]])

MEAN = df.loc[(df[atribute_list[14]] <= 75) & (df[atribute_list[14]] != 0),atribute_list[14]].mean()
df.loc[(df[atribute_list[14]] > 75) | (df[atribute_list[14]] == 0),atribute_list[14]] = int(MEAN)
df.loc[(df[atribute_list[14]] <0),atribute_list[14]] = int(MEAN)
df[atribute_list[14]].value_counts().to_csv("age")

df[atribute_list[15]] = df[atribute_list[15]].replace(["?"],"Other")
df[atribute_list[15]].value_counts().to_csv("other_payment_plans")

df[atribute_list[16]] = df[atribute_list[16]].replace(["?"],"Other")

df[atribute_list[16]].value_counts().to_csv("housing")

df[atribute_list[17]] = df[atribute_list[17]].replace(["?"],"0")
df[atribute_list[17]].value_counts().to_csv("existing_credits")

df[atribute_list[18]] = df[atribute_list[18]].replace(["?"],"Other")
df[atribute_list[18]].value_counts().to_csv("job")

df.loc[(df[atribute_list[19]] != '1') & (df[atribute_list[19]] != '2'),atribute_list[19]] = "Unknown"
df[atribute_list[19]].value_counts().to_csv("num_dependents")

df[atribute_list[20]] = df[atribute_list[20]].replace(["?"],"no")
df[atribute_list[20]].value_counts().to_csv('own_telephone')

df[atribute_list[21]] = df[atribute_list[21]].replace(['N'],'no')
df[atribute_list[21]] = df[atribute_list[21]].replace(['No'],'no')
df[atribute_list[21]] = df[atribute_list[21]].replace(['NO'],'no')
df[atribute_list[21]] = df[atribute_list[21]].replace(['n'],'no')
df[atribute_list[21]] = df[atribute_list[21]].replace(['Yes'],'yes')
df[atribute_list[21]] = df[atribute_list[21]].replace(['YES'],'yes')
df[atribute_list[21]] = df[atribute_list[21]].replace(['Y'],'yes')
df[atribute_list[21]] = df[atribute_list[21]].replace(['y'],'yes')
df[atribute_list[21]] = df[atribute_list[21]].replace(['Y'],'yes')
df[atribute_list[21]] = df[atribute_list[21]].replace(['1'],'Unknown')
df[atribute_list[21]] = df[atribute_list[21]].replace(['?'],'Unknown')
df[atribute_list[21]].value_counts().to_csv('foreign_worker')

df[atribute_list[22]] = df[atribute_list[22]].replace(['GOOD'],'Good')
df[atribute_list[22]] = df[atribute_list[22]].replace(['good'],'Good')
df[atribute_list[22]] = df[atribute_list[22]].replace(['G'],'Good')
df[atribute_list[22]] = df[atribute_list[22]].replace(['bad'],'Bad')
df[atribute_list[22]] = df[atribute_list[22]].replace(['B'],'Bad')
df[atribute_list[22]] = df[atribute_list[22]].replace(['?'],'Good')
df[atribute_list[22]].value_counts().to_csv("class")

df[atribute_list[25]] = df[atribute_list[25]].replace(['N'],'no')
df[atribute_list[25]] = df[atribute_list[25]].replace(['No'],'no')
df[atribute_list[25]] = df[atribute_list[25]].replace(['NO'],'no')
df[atribute_list[25]] = df[atribute_list[25]].replace(['n'],'no')
df[atribute_list[25]] = df[atribute_list[25]].replace(['Yes'],'yes')
df[atribute_list[25]] = df[atribute_list[25]].replace(['YES'],'yes')
df[atribute_list[25]] = df[atribute_list[25]].replace(['y'],'yes')
df[atribute_list[25]] = df[atribute_list[25]].replace(['Y'],'yes')
df[atribute_list[25]] = df[atribute_list[25]].replace(['1'],'Unknown')
df[atribute_list[25]] = df[atribute_list[25]].replace(['?'],'Unknown')
df[atribute_list[25]].value_counts().to_csv('work_outside')

# Set MM/DD/YYYY as date format.  
df['application_date'] = pd.to_datetime(df.application_date)
df['application_date'] = df['application_date'].dt.strftime('%m/%d/%Y')
df = df.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24]]

def Chi_square_test(data_frame):
  ##dof = (row-1)*(cols-1)
  sig = 0.05
  chi, pval, dof, exp = chi2_contingency(data_frame)
  p = 1 - sig
  critical_value = chi2.ppf(p,dof)

  if(chi > critical_value):

      return "N"
  else:
      return "I"

atribut_list = list(df.columns)
""" atribut_list = ['location','state','credit_history','purpose','employment','installment_commitment',\
                'personal_status','other_parties','residence_since','property_magnitude','housing','job',\
                'num_dependents','own_telephone','foreign_worker','class'] """
                
Chi_fram = pd.DataFrame(columns = atribut_list, index=atribut_list)

X = df.copy()
V = []
for i in range(0,len(atribut_list)):
   for j in range(i+1,len(atribut_list)):
        Add_list = X.groupby([atribut_list[i],atribut_list[j]])[[atribut_list[j]]].count().unstack().fillna(0)
        V.append(Add_list)

count = 0
for i in range(0,len(atribut_list)):
   for j in range(i+1,len(atribut_list)):
        Chi_fram.iloc[i,j] = Chi_square_test(V[count])
        count = count + 1

Chi_fram.to_csv('I_test.csv')

def spear_val(row_index, col_index,DataFrame_1,list_value):

    X1 =  DataFrame_1.loc[:,list_value[row_index]].values.reshape(-1,1)
    Y1 =  DataFrame_1.loc[:,list_value[col_index]].values.reshape(-1,1)
    corr, p_value = spearmanr(X1,Y1)

    if((np.abs(corr) >= 0.8)):
        return "N"
    else:
        return "I"


atribut_list2 = ['checking_amt','duration','credit_amount','savings','age']
spear_fram = pd.DataFrame(columns = atribut_list2, index=atribut_list2)

for i in range(0,len(atribut_list2)):
    for j in range(i+1,len(atribut_list2)):
        spear_fram.iloc[i,j] = spear_val(i,j,X,atribut_list2)

print(spear_fram)
spear_fram.to_csv("spea_fram.csv")

df.to_csv('cleaned_credit.csv', index=False)