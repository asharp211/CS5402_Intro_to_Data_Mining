import numpy as np, pandas as pd
from sklearn import preprocessing
import yaml
from pomegranate import *

#df = pd.read_csv('contact-lenses.csv')
df = pd.read_csv('hypothyroid.csv')

# Making the Column index
col_list = []
for i in df:
    col_list.append(i)

#print(col_list)

# Lambda is always equal to 1
_lambda = 1

def myMap(df, col_list):
    atr = {}
    for i in df[col_list]:
        atr[i] = i
    return list(atr)

# Laplace Smoothing 
# P(x1 = aj | y = Ck) = (sum(I*(x1 = aj, y = Ck) + Lambda)/()
# 
def ConditionalProbabilityT(x1, A1, y1, A2, k):
    Top = df.loc[(df[x1] == A1) & (df[y1] == A2),:].index.size
    Bot = df.loc[(df[x1] == A1),:].index.size
    
    return (Top + _lambda)/(Bot+ k * _lambda)


def Bayesian_Network(dataframe, title):
    num_size = dataframe.index.size
    P = []
    model = BayesianNetwork(title)

    decision_str = col_list[len(col_list) - 1]

    #print("decision", decision_str)
    dictionary = {}
    #k = len(myMap(dataframe, decision_str))
    for i in myMap(dataframe, decision_str):
        k = len(myMap(dataframe, decision_str))
        dictionary[i] = ((dataframe.loc[dataframe[decision_str] == i,:].index.size)+(_lambda))/(num_size+k*_lambda)
    
    # Table for discrete Distrubtion(isn't conditional on any other nodes)
    P.append(DiscreteDistribution(dictionary))
    #print(P)
    for i in range(0,len(col_list)-1):
        con = []
        L = len(myMap(dataframe, col_list[i]))
        for j in myMap(dataframe, decision_str):
            for k in myMap(dataframe, col_list[i]):
                con.append([j,k,
                ConditionalProbabilityT(decision_str, k, col_list[i], k, L)])
        
        C = ConditionalProbabilityTable(con, [P[0]])

        P.append(C)
        #print(P)
    
    # Create nodes with their probability tables
    s1 = Node(P[0], name=decision_str)

    #model.add_states(s1, s2, s3, s4, s5) # add the nodes
    model.add_state(s1)

    # add the nodes and edges
    for i in range(1, len(P)):
        s2 = Node(P[i], name = col_list[i-1])
        model.add_state(s2)
        model.add_edge(s1,s2)
    
    model.bake()
    return model

in_model = Bayesian_Network(df,"Bayesian Network")
#print(in_model)
# Hardcode Prediction
# sex,on_thyroxine,on_antithyroid_medication,thyroid_surgery,lithium,goitre,hypopituitary,psych,referral_source,Class
'''testing'''
#instance = ['negative','M','f','f','f','f','f','f','t','SVHC']
instance = ['primary_hypothyroid',"M",None,None,None,None,None,None,None,'SVI']

# From Leopold's notes below
likelihood_yes = in_model.probability([instance])
print("instance: " , instance)
print("likelihood_yes" , likelihood_yes)
instance[0] = 'negative'
likelihood_no = in_model.probability([instance])
print("likelihood_no" , likelihood_no)
prob_yes = (likelihood_yes / (likelihood_yes + likelihood_no))* 100
prob_no = (likelihood_no / (likelihood_yes + likelihood_no))* 100
print(prob_yes, prob_no)