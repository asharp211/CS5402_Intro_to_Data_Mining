import numpy as np
import pandas as pd

df = pd.read_csv("breast-cancer.csv")

def Data_slicer(data_fame,logic_string,atribute_string,value):

        logic_operator_str = logic_string
        if(logic_string == "<"):

            return df.loc[df[atribute_string] < value,:]
        elif(logic_string == "<="):

            return df.loc[df[atribute_string] <= value,:]
        elif(logic_string=='>'):

            return df.loc[df[atribute_string] > value,:]

        elif(logic_string == ">="):

            return df.loc[df[atribute_string] >= value,:]

        elif(logic_string == "=="):

            return df.loc[df[atribute_string] == value,:]

        elif(logic_string == "!="):
            return df.loc[df[atribute_string] != value,:]

#logical intersection of a set of subsets in data_fram
def merge_frames(Data_list_frame22):
    List_size_22 = len(Data_list_frame22)
    New_data_frame = pd.merge(Data_list_frame22[0],Data_list_frame22[1],how= 'inner')

    for i in range(2,List_size_22):
        New_data_frame = pd.merge(New_data_frame,Data_list_frame22[i],how='inner')

    return New_data_frame

Test_list = [[0,1,420],[5,2,0.5],[16,2,250],[21,4,2]]
"""
test_1 = df.loc[df.age=='40-49',:]
test_2 = df.loc[df["tumor-size"]=='0-4',:]
test_3 = df.loc[df["inv-nodes"]=='0-2',:]
test_4 = df.loc[df["node-caps"]=='no',:]"""

test_1 = Data_slicer(df,'==',"tumor-size",'0-4')
test_2 = Data_slicer(df,'==','age','40-49')
test_3 = Data_slicer(df,'==',"inv-nodes",'0-2')
test_4 = Data_slicer(df,"==","node-caps",'no')

F = [test_1,test_2,test_3,test_4]

V = merge_frames(F)

RULES = [[2,4,"0-4"],[0,4,"40-49"],[4,4,"no"],[3,4,"0-2"],[9,4,"no-recurrence-events"]]

def rule_optimised(data_fram,rule,confidence_level=0.5):

    Logic_regular =  ["<","<=",">",">=","==","!="]
    Nagated_logic = [">=",">","<=","<",'!=','==']

    atribute_list = list(data_fram.columns)
    Count_instants = pd.DataFrame(columns = ["Y1","Y2","E1","E2"])
    list_e  = []   #atribute list for data_fram

    for atributes in data_fram:

        list_e.append(atributes)

    length_of_rule = len(rule)
    consiquence_index = rule[length_of_rule-1]

    Atrubutes_in_rule = []

    for each_atrubute in rule:
        Atrubutes_in_rule.append(list_e[each_atrubute[0]])

    Count_instants = pd.DataFrame(columns = ["Y1","Y2","E1","E2"],index = Atrubutes_in_rule)

    #Count_instants.index = Atrubutes_in_rule   #### makes row indexs for contigency table

    for atrubute_in_Contin in Count_instants.index:

            Y_data_fram_list = []
            E_data_fram_list = []
            count_1 = 0
             ## starting at nagative not aticidene is nigated first round
            for each in rule:
                if (count_1 == length_of_rule - 1):   ## hits consiquent index

                    E_data_fram_list.append(Data_slicer(data_fram,Nagated_logic[each[1]],list_e[each[0]],each[2]))

                else:

                    E_data_fram_list.append(Data_slicer(data_fram,Logic_regular[each[1]],list_e[each[0]],each[2]))

                Y_data_fram_list.append(Data_slicer(data_fram,Logic_regular[each[1]],list_e[each[0]],each[2]))

                count_1 = count_1 + 1  # keeps track of index of rule
				
            DATA_FRAME33 = merge_frames(Y_data_fram_list)
            DATA_FRAME332 = merge_frames(E_data_fram_list)

            Count_instants.loc[atrubute_in_Contin,"Y1"] = DATA_FRAME33.index.size

            Count_instants.loc[atrubute_in_Contin,"E1"] = DATA_FRAME332.index.size



    count_2 = 0
    for atrubute_in_Contin in Count_instants.index:

           Y_data_fram_list = []
           E_data_fram_list = []
           count_1 = 0
                  ## starting at nagative not aticidene is nigated first round
           for each in rule:

                if(count_1 != count_2):

                     if (count_1 == length_of_rule - 1):   ## hits consiquent index

                         E_data_fram_list.append(Data_slicer(data_fram,Nagated_logic[each[1]],list_e[each[0]],each[2]))

                     else:

                         E_data_fram_list.append(Data_slicer(data_fram,Logic_regular[each[1]],list_e[each[0]],each[2]))

                     Y_data_fram_list.append(Data_slicer(data_fram,Logic_regular[each[1]],list_e[each[0]],each[2]))

                     count_1 = count_1 + 1  # keeps track of index of rule
                else:


                     if (count_1 == length_of_rule - 1):   ## hits consiquent index

                         E_data_fram_list.append(Data_slicer(data_fram,Nagated_logic[each[1]],list_e[each[0]],each[2]))

                     else:

                         E_data_fram_list.append(Data_slicer(data_fram,Nagated_logic[each[1]],list_e[each[0]],each[2]))

                     Y_data_fram_list.append(Data_slicer(data_fram,Nagated_logic[each[1]],list_e[each[0]],each[2]))

                     count_1 = count_1 + 1  # keeps track of index of rule

           count_2 = count_2 + 1
		   
           DATA_FRAME33 = merge_frames(Y_data_fram_list)
           DATA_FRAME332 = merge_frames(E_data_fram_list)
           print(DATA_FRAME33)
           print("________")
           print(DATA_FRAME332)

           Count_instants.loc[atrubute_in_Contin,"Y2"] = DATA_FRAME33.index.size
           Count_instants.loc[atrubute_in_Contin,"E2"] = DATA_FRAME332.index.size

    print(Count_instants)

rule_optimised(df,RULES)
