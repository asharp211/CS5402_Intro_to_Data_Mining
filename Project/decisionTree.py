'''
ID3/J48 or SimpleCart
'''
from sklearn import tree
import pandas as pd
import numpy
import graphviz

df = pd.read_csv('decision.csv')

r,c = df.shape

#check LazyProgram.py for this
""" df= df.replace({'state': r'Pennsylvania'}, {'state':0}, regex=True)
df= df.replace({'state': r'Rhodes Island'}, {'state':1}, regex=True)
df= df.replace({'state': r'South Carolina'}, {'state':2}, regex=True)
df= df.replace({'state': r'South Dakota'}, {'state':3}, regex=True)
df= df.replace({'state': r'Tennessee'}, {'state':4}, regex=True)
df= df.replace({'state': r'Texas'}, {'state':5}, regex=True)
df= df.replace({'state': r'Utah'}, {'state':6}, regex=True)
df= df.replace({'state': r'Virginia'}, {'state':7}, regex=True)
df= df.replace({'state': r'Vermont'}, {'state':8}, regex=True)
df= df.replace({'state': r'Washington'}, {'state':9}, regex=True)
df= df.replace({'state': r'Wisconsin'}, {'state':10}, regex=True)
df= df.replace({'state': r'West Virginia'}, {'state':11}, regex=True)
df= df.replace({'state': r'Wyoming'}, {'state':12}, regex=True)
df= df.replace({'state': r'Alaska'}, {'state':13}, regex=True)
df= df.replace({'state': r'Arkansas'}, {'state':14}, regex=True)
df= df.replace({'state': r'Arizona'}, {'state':15}, regex=True)
df= df.replace({'state': r'California'}, {'state':16}, regex=True)
df= df.replace({'state': r'Colorado'}, {'state':17}, regex=True)
df= df.replace({'state': r'Connecticut'}, {'state':18}, regex=True)
df= df.replace({'state': r'District of Columbia'}, {'state':19}, regex=True)
df= df.replace({'state': r'Delaware'}, {'state':20}, regex=True)
df= df.replace({'state': r'Georgia'}, {'state':21}, regex=True)
df= df.replace({'state': r'Hawaii'}, {'state':22}, regex=True)
df= df.replace({'state': r'Illinois'}, {'state':23}, regex=True)
df= df.replace({'state': r'Indiana'}, {'state':24}, regex=True)
df= df.replace({'state': r'Kentucky'}, {'state':25}, regex=True)
df= df.replace({'state': r'Louisiana'}, {'state':26}, regex=True)
df= df.replace({'state': r'Massachusetts'}, {'state':27}, regex=True)
df= df.replace({'state': r'Maryland'}, {'state':28}, regex=True)
df= df.replace({'state': r'Michigan'}, {'state':29}, regex=True)
df= df.replace({'state': r'Missouri'}, {'state':30}, regex=True)
df= df.replace({'state': r'Mississippi'}, {'state':31}, regex=True)
df= df.replace({'state': r'North Carolina'}, {'state':32}, regex=True)
df= df.replace({'state': r'New Hampshire'}, {'state':33}, regex=True)
df= df.replace({'state': r'New Jersey'}, {'state':34}, regex=True)
df= df.replace({'state': r'New Mexico'}, {'state':35}, regex=True)
df= df.replace({'state': r'Nevada'}, {'state':36}, regex=True)
df= df.replace({'state': r'New York'}, {'state':37}, regex=True)
df= df.replace({'state': r'Ohio'}, {'state':38}, regex=True)
df= df.replace({'state': r'Oregon'}, {'state':39}, regex=True)
df= df.replace({'state': r'Alabama'}, {'state':40}, regex=True)
df= df.replace({'state': r'Florida'}, {'state':41}, regex=True)
df= df.replace({'state': r'Iowa'}, {'state':42}, regex=True)
df= df.replace({'state': r'Idaho'}, {'state':43}, regex=True)
df= df.replace({'state': r'Kansas'}, {'state':44}, regex=True)
df= df.replace({'state': r'Maine'}, {'state':45}, regex=True) """

df= df.replace({'housing': r'own'}, {'housing':0}, regex=True)
df= df.replace({'housing': r'for free'}, {'housing':1}, regex=True)
df= df.replace({'housing': r'rent'}, {'housing':2}, regex=True)
df= df.replace({'housing': r'Other'}, {'housing':3}, regex=True)

df= df.replace({'job': r'skilled'}, {'job':0}, regex=True)
df= df.replace({'job': r'unskilled resident'}, {'job':1}, regex=True)
df= df.replace({'job': r'high qualif/self emp/mgmt'}, {'job':2}, regex=True)
df= df.replace({'job': r'unemp/unskilled non res'}, {'job':3}, regex=True)
df= df.replace({'job': r'Other'}, {'job':4}, regex=True)

df= df.replace({'foreign_worker': r'no'}, {'foreign_worker':0}, regex=True)
df= df.replace({'foreign_worker': r'yes'}, {'foreign_worker':1}, regex=True)
df= df.replace({'foreign_worker': r'unknown'}, {'foreign_worker':2}, regex=True)

X = df.iloc[:, 0:c-1].values
y = df.iloc[:, c-1].values

clf = tree.DecisionTreeClassifier(criterion="gini")
clf = clf.fit(X, y)

attrNames = list(df.columns)

classNames = numpy.array(list(set(df["class"].values)))
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=attrNames[0:c-1],
                                class_names=classNames,
                                filled=True, 
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("Class_Decision_Tree")
tree.plot_tree(clf.fit(X, y))