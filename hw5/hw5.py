import copy
import statsmodels.api as sm
from statsmodels.stats.proportion import proportion_confint
#import numexpr as ne
import pandas as pd
import numpy as np
#import csv

df = pd.read_csv("breast-cancer1.csv")
f = open('rules_in_List.txt','r+')

# 50-59,lt40,20-24,    0-2,?,1,   left,left_low,no,recurrence-events

#    int  int float , int int float, int int float
# [[[4, 4, 'yes'], [5, 4, '1']], [[9, 4, 'recurrence-events']]]

# [attributeIndexNumber, operatorCode, value]
# [[[AIT203 = 0, operatorCode = 1, AIT203 <= 420]  ,[FIT201 = 5, 2, FIT201 = 0.5]]]

'''
Every row of the table
Y1 = A1, A2, A3, A4, AND C
E1 = A1, A2, A3, A4, AND !C

Row 1
Y2 = !A1, A2, A3, A4, AND C
E2 = !A1, A2, A3, A4, AND !C

Row 2 
Y2 = A1, !A2, A3, A4, AND C
E2 = A1, !A2, A3, A4, AND !C

...
calc y1 and e1 once
loop the y2 and e2...

#for the fails only
Rule original
1 - U(cf)(y1, y1+e2)

Rules with condition drop
1 - U(cf)(y1+y2, y1 + e1 + y2 + e2)
'''


outer_row_list = []
for row in df:
    outer_row_list.append(row)
# outer_row_list = ['age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat', 'Class']
#print(outer_row_list)


""" print(df.loc[df["tumor-size"] < '0-4',:])
print(df.loc[df["age"] < '40-49',:]) """

#Data_slicer(df,'==',"tumor-size",'0-4')
def Logic_Rule(atribute,_logic,value):
    if(_logic == "<"):
        return df.loc[df[atribute] < value,:]

    elif(_logic == "<="):
        return df.loc[df[atribute] <= value,:]

    elif(_logic=='>'):
        return df.loc[df[atribute] > value,:]

    elif(_logic == ">="):
        return df.loc[df[atribute] >= value,:]

    elif(_logic == "=="):
        return df.loc[df[atribute] == value,:]

    elif(_logic == "!="):
        return df.loc[df[atribute] != value,:]

# A must to merge dataframe together
def merge_frame(f):
    _size = len(f)
    newDataFrame = pd.merge(f[0],f[1], how='inner')
    for i in range(_size):
        newDataFrame = pd.merge(newDataFrame,f[i], how='inner')  
    return newDataFrame
""" 
def efficientRule(rule, confLevel):
   
    confLevel = float(confLevel/100)
    
    # Build list the conditions in the antecedent
    allConditions = rule[0]
    
    # Variable to store opimized rule
    newRule = copy.deepcopy(rule[0])
    anticedentLength = len(allConditions)
    consequent = rule[1]
    allConditions.append(consequent[0])
    
    # Dataframe used to process csv file
    boolData = pd.DataFrame()
    
    # Contingency table to hold Y1 E1
    contingencyTable = []

    # Arguments of proportion_confint(Number of "successes", # Number of trials, alpha=(1 - 0.95), method='beta')
    Ux = proportion_confint(15, 16, alpha=(1 -0.95), method='beta')
    print("\n\nThe interval for ux is:", Ux)
    Ux = 1 - float(Ux[0]) 
    print("Ux is type: ",type(Ux))
    print("The value of Ux is", Ux)
    contTable.append([15, 1, Ux])
    print("ContTable is", contTable)

    Ux = proportion_confint(9, 11, alpha=(1 -0.90), method='beta')
    print("\n\nThe interval for ux is:", Ux)
    Ux = 1 - float(Ux[0]) 
    print("Ux is type: ",type(Ux))
    print("The value of Ux is", Ux)
    contTable.append([9, 2, Ux])
    print("ContTable is", contTable)

    Ux = proportion_confint(17, 20, alpha=(1 -0.90), method='beta')
    print("\n\nThe interval for ux is:", Ux)
    Ux = 1 - float(Ux[0]) 
    print("Ux is type: ",type(Ux))
    print("The value of Ux is", Ux)
    contTable.append([17, 3, Ux])
    print("ContTable is", contTable)

    U_CF1 = proportion_confint(Y1+Y2, Y1+E1+Y2+E2, alpha=(1 - confLevel), method='beta')
    U_CF1 = 1 - float(U_CF1[0]) 
    print("UCF1 is type: ",type(U_CF1))
    print("The value of U_CF1 is", U_CF1)
    contingencyTable.append([Y1, E1, U_CF1])

    print("boolDate before dropping last", boolData)
    #Drop the last column with counts of Y1 and E1
    boolData = boolData.iloc[:, :-1]
    print("boolDate after dropping last", boolData)

    # for index in range(boolData.shape[1]):
    #     boolData[index] = boolData.apply(bitwiseNot, axis=1)
 """


# START HERE!!!!
# hardcode
test_case = [[0, 1, 420], [5, 2, 0.5], [16, 2, 250]], [[21, 4, 2]]      #420 Blaze it!!!

test_rule = [[2,4,"0-4"],[0,4,"40-49"],[4,4,"no"],[3,4,"0-2"],[9,4,"no-recurrence-events"]]

test1 = Logic_Rule('tumor-size','==','0-4')
test2 = Logic_Rule('age','==','40-49')
test3 = Logic_Rule('inv-nodes','==','0-2')
test4 = Logic_Rule('node-caps','==','no')

test_rule2 = [[[4, 4, 'yes'], [5, 4, '1']], [[9, 4, 'recurrence-events']]]
""" test5 = Logic_Rule('node-caps','==','yes')
test6 = Logic_Rule('deg-malig','==','1')
test7 = Logic_Rule('class','==','recurrence-events') """

test_rule3 = [[[4, 4, 'no'], [3, 4, '0-2'], [2, 4, '0-4']], [[9, 4, 'no-recurrence-events']]]


test_rule4 = [[4, 4, 'yes'], [5, 4, '2'], [2, 4, '30-34'], [7, 4, 'central']], [[9, 4, 'recurrence-events']]


test_rule5 = [[4, 4, 'yes'], [5, 4, '2'], [2, 4, '50-54']], [[9, 4, 'no-recurrence-events']]

ruleLength = len(test_rule)

operatorCode = ["<","<=",">",">=","==","!="]

#print(len(test_case))

frame1 = [test1, test2, test3, test4]
#fram2 = [test5, test6, test7]

#   Call to merge frame
M = merge_frame(frame1)


attribute = []
for i in df:
    attribute.append(i)

attributeRow = []

for i in test_rule:
    attributeRow.append(attribute[i[0]])

change_R_and_C = pd.DataFrame(columns = ["Y1","Y2","E1","E2"], index = attributeRow)

for i in change_R_and_C.index:
    _Y = []
    _E = []

    count1 = 0

    for j in test_rule:
        if(count1 == ruleLength-1):
            #Logic_Rule('age','==','40-49')
            _E.append(Logic_Rule(attribute[j[0]],operatorCode[j[1]],j[2]))
        
        else:
            _E.append(Logic_Rule(attribute[j[0]],operatorCode[j[1]],j[2]))
    
        _Y.append(Logic_Rule(attribute[j[0]],operatorCode[j[1]],j[2]))

        count1 += 1
    
    mergeY = merge_frame(_Y)
    mergeE = merge_frame(_E)

    change_R_and_C.loc[i,"Y1"] = mergeY.index.size
    change_R_and_C.loc[i,"E1"] = mergeE.index.size

count2 = 0
for i in change_R_and_C.index:
    _Y = []
    _E = []

    count1 = 0

    for j in test_rule:
        if(count1 != count2):
            if(count1 == ruleLength-1):
                _E.append(Logic_Rule(attribute[j[0]],operatorCode[j[1]],j[2]))
        
            else:
                _E.append(Logic_Rule(attribute[j[0]],operatorCode[j[1]],j[2]))
        
            _Y.append(Logic_Rule(attribute[j[0]],operatorCode[j[1]],j[2]))

            count1 += 1
        else:
            if(count1 == ruleLength-1):
                _E.append(Logic_Rule(attribute[j[0]],operatorCode[j[1]],j[2]))
        
            else:
                _E.append(Logic_Rule(attribute[j[0]],operatorCode[j[1]],j[2]))
        
            _Y.append(Logic_Rule(attribute[j[0]],operatorCode[j[1]],j[2]))

            count1 += 1
    count1 += 1

    mergeY = merge_frame(_Y)
    mergeE = merge_frame(_E)

    change_R_and_C.loc[i,"Y2"] = mergeY.index.size
    change_R_and_C.loc[i,"E2"] = mergeE.index.size

print(change_R_and_C)