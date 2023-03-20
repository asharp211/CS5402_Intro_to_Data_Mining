from sklearn import tree
import pandas as pd
import numpy
import graphviz


df = pd.read_csv('Trading.csv')
r,c = df.shape

# Non-decision attr's have to be numeric!

df= df.replace({'PastTrend': r'Positive'}, {'PastTrend':1}, regex=True)
df= df.replace({'PastTrend': r'Negative'}, {'PastTrend':-1}, regex=True)
df= df.replace({'OpenInterest': r'Low'}, {'OpenInterest':0}, regex=True)
df= df.replace({'OpenInterest': r'High'}, {'OpenInterest':1}, regex=True)
df= df.replace({'TradingVol': r'Low'}, {'TradingVol':0}, regex=True)
df= df.replace({'TradingVol': r'High'}, {'TradingVol':1}, regex=True)


X = df.iloc[:, 0:c-1].values # non-decision attributes
y = df.iloc[:, c-1].values # decision attribute


clf = tree.DecisionTreeClassifier(criterion="gini")
clf = clf.fit(X, y)
attrNames = list(df.columns)
classNames = numpy.array(list(set(df["Return"].values)))
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=attrNames[0:c-1],
                                class_names=classNames,
                                filled=True, 
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("Trading_Decision_Tree")
tree.plot_tree(clf.fit(X, y))

# see Trading_Decision_Tree.pdf