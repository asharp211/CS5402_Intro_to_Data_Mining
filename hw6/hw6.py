import numpy as np, pandas as pd
import yaml
from pomegranate import *

df = pd.read_csv('contact-lenses.csv')

col_list = []
for i in df:
    col_list.append(i)

print(col_list)

#print(df)

# Table for Play is discrete (isn't conditional on any other nodes)
P = DiscreteDistribution({'yes': 0.633, 'no': 0.367})
# Table for Outlook is conditional on Play
# Columns in the table correspond to Play, Outlook prob's
O = ConditionalProbabilityTable(
    [['yes', 'sunny', 0.238],
    ['yes', 'overcast', 0.429],
    ['yes', 'rainy', 0.333],
    ['no', 'sunny', 0.538],
    ['no', 'overcast', 0.077],
    ['no', 'rainy', 0.385]],
    [P])

# Table for Windy is conditional on Play
# Columns in the table correspond to Play, Windy prob's
W = ConditionalProbabilityTable(
    [['yes', 'false', 0.350],
    ['yes', 'true', 0.650],
    ['no', 'false', 0.583],
    ['no', 'true', 0.417]],
    [P])

# Table for Temperature is conditional on Play
# Columns in the table correspond to Play, Temperature prob's
T = ConditionalProbabilityTable(
 [['yes', 'hot', 0.238],
 ['yes', 'mild', 0.429],
 ['yes', 'cool', 0.333],
 ['no', 'hot', 0.385],
 ['no', 'mild', 0.385],
 ['no', 'cool', 0.231]],
 [P])

# Table for Humidity is conditional on Play
# Columns in the table correspond to Play, Humidity prob's
H = ConditionalProbabilityTable(
 [['yes', 'high', 0.350],
 ['yes', 'normal', 0.650],
 ['no', 'high', 0.750],
 ['no', 'normal', 0.250]],
 [P])

# Create nodes with their probability tables
s1 = Node(P, name="Play")
print(s1)
s2 = Node(O, name="Outlook")
s3 = Node(W, name="Windy")
s4 = Node(T, name="Temperature")
s5 = Node(H, name="Humidity")

model = BayesianNetwork("Weather Bayesian Network")
model.add_states(s1, s2, s3, s4, s5) # add the nodes
model.add_edge(s1, s2) # add the edges
model.add_edge(s1, s3)
model.add_edge(s1, s4)
model.add_edge(s1, s5)
model.bake() # actually create the network

# Can now make predictions
# Order of list is [Play, Outlook, Windy, Temperature, Humidity]
# i.e., same as order nodes were created
instance = ['yes', 'rainy', 'true', 'cool', 'high']
likelihood_yes = model.probability([instance])
print("instance: " , instance)
print("Here")
print("Likelyhood" , likelihood_yes)
instance[0] = 'no'
likelihood_no = model.probability([instance])
prob_yes = (likelihood_yes / (likelihood_yes + likelihood_no))* 100
prob_no = (likelihood_no / (likelihood_yes + likelihood_no))* 100
print(prob_yes, prob_no)

# Here it will predict the None's
print(model.predict([['yes', 'rainy', None, None, None]]))

