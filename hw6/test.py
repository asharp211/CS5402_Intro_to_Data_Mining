import numpy as np, pandas as pd
import yaml
from pomegranate import *

df = pd.read_csv('hypothyroid.csv')

def map_value(df, atribute_str):
    dix = {}
    for i in df[atribute_str]:
        dix[i] = i
    return list(dix)

def condition_prob(atribute1, value1, atribute2, value2, k, lambda1):
    Top = df.loc[(df[atribute1] == value1) & (df[atribute2]==value2),:].index.size
    
    Bottom = df.loc[(df[atribute1] == value1),:].index.size
   
    return (Top + lambda1)/(Bottom + k*lambda1)

def Bayesian_Network(dataframe, lambdaa = 1, title=''):
    N = dataframe.index.size
    distrbution_list = []
    atribute_list = list(dataframe.columns) 

    model = BayesianNetwork(title)

    Decsion_atribute_str = atribute_list[len(atribute_list) -1]
    Dictionary1 = {}
    for each in map_value(dataframe, Decsion_atribute_str):
        K = len(map_value(dataframe,Decsion_atribute_str))
        Dictionary1[each] = ((dataframe.loc[dataframe[Decsion_atribute_str]==each,:]\
        .index.size)+(lambdaa))/(N+K*lambdaa)

    distrbution_list.append(DiscreteDistribution(Dictionary1))

    for i in range(0, len(atribute_list)-1):
        list2 = []
        for j in map_value(dataframe, Decsion_atribute_str):
            for k in map_value(dataframe, atribute_list[i]):
                list2.append([j,k,condition_prob(Decsion_atribute_str,k,
                atribute_list[i],k,len(map_value(dataframe, atribute_list[i])), lambdaa)])

        G = ConditionalProbabilityTable(list2, [distrbution_list[0]])

        distrbution_list.append(G)
    #
    # model = BayesianNetwork(title)
    S1 = Node(distrbution_list[0], name=Decsion_atribute_str)
    model.add_state(S1)

    for i in range(1, len(distrbution_list)):
        S = Node(distrbution_list[i],name= atribute_list[i-1])
        model.add_state(S)
        model.add_edge(S1,S)

    model.bake()
    return model

new_model = Bayesian_Network(df,1,"name of ... ")
# Here it will predict the None's
print('input: ', ['negative',None,None,None,None,None,None,None,None,None])
print(new_model.predict([['negative',None,None,None,None,None,None,None,None,None]]))

print('input: ', ['primary_hypothyroid',"M",None,None,None,None,None,None,None,'SVI'])
print(new_model.predict([['primary_hypothyroid',"M",None,None,None,None,None,None,None,'SVI']]))
