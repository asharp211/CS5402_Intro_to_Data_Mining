'''
Anthony Sharp
AVSRCM
Sept-20-2020
'''

from sklearn import tree
import pandas as pd
import numpy
import graphviz     #pip install graphviz

df = pd.read_csv('candy.csv')
print(df) 

r,c = df.shape

df= df.replace({'consistency': r'soft'}, {'consistency':0}, regex=True)
df= df.replace({'consistency': r'hard'}, {'consistency':1}, regex=True)
df= df.replace({'packaging': r'individuallyWrapped'}, {'packaging':0}, regex=True)
df= df.replace({'packaging': r'box'}, {'packaging':1}, regex=True)
df= df.replace({'chocolate': r'no'}, {'chocolate':0}, regex=True)
df= df.replace({'chocolate': r'yes'}, {'chocolate':1}, regex=True)

X = df.iloc[:, 0:c-1].values
y = df.iloc[:, c-1].values

clf = tree.DecisionTreeClassifier(criterion="gini")
clf = clf.fit(X, y)

attrNames = list(df.columns)

classNames = numpy.array(list(set(df["isSticky"].values)))
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=attrNames[0:c-1],
                                class_names=classNames,
                                filled=True, 
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("Candy_Decision_Tree")
tree.plot_tree(clf.fit(X, y))