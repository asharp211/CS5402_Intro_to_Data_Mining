'''
Anthony Sharp
AVSRCM
Sept-20-2020
'''

from sklearn import tree
import pandas as pd
import numpy
import graphviz     #pip install graphviz

df = pd.read_csv('restaurant.csv')
print(df) 

r,c = df.shape

df= df.replace({'ageGroup': r'young'}, {'ageGroup':0}, regex=True)
df= df.replace({'ageGroup': r'middle'}, {'ageGroup':1}, regex=True)
df= df.replace({'ageGroup': r'senior'}, {'ageGroup':2}, regex=True)
df= df.replace({'gender': r'm'}, {'gender':1}, regex=True)
df= df.replace({'gender': r'f'}, {'gender':0}, regex=True)
df= df.replace({'married': r'no'}, {'married':0}, regex=True)
df= df.replace({'married': r'yes'}, {'married':1}, regex=True)
#df= df.replace({'restaurant': r'mcdonals'}, {'restaurant':0}, regex=True)
#df= df.replace({'restaurant': r'wendys'}, {'restaurant':1}, regex=True)
#df= df.replace({'restaurant': r'burgerKing'}, {'restaurant':2}, regex=True)

X = df.iloc[:, 0:c-1].values
y = df.iloc[:, c-1].values

clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(X, y)

attrNames = list(df.columns)

classNames = numpy.array(list(set(df["restaurant"].values)))
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=attrNames[0:c-1],
                                class_names=classNames,
                                filled=True, 
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("Restaurant_Decision_Tree")
tree.plot_tree(clf.fit(X, y))