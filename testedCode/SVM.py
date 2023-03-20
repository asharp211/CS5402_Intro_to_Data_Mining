import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
df = pd.read_csv('svm_exampleData.csv')
# Just for graphing purposes, change non-decision attr's
# to have numeric values
df= df.replace({'z': r'positive'}, {'z':1}, regex=True)
df= df.replace({'z': r'negative'}, {'z':-1}, regex=True)
X = df.iloc[:, 0:2].values
y = df.iloc[:, 2].values
r,_ = df.shape
# Display original data points
plt.scatter(X[:, 0], X[:, 1], c=y, s=r, cmap='winter');
plt.show()
# Make a linear SVM
model = SVC(kernel='linear')
model.fit(X, y)
print(model.support_vectors_) # The support vectors
print(model.coef_) # The weights (x and y)
print(model.intercept_) # The intercept
7
# Function to plot SVM boundary lines - cool!
def plot_svc_decision_function(model, ax=None, plot_support=True):
 if ax is None:
    ax = plt.gca()
 xlim = ax.get_xlim()
 ylim = ax.get_ylim()

 # Create grid to evaluate model
 x = np.linspace(xlim[0], xlim[1], 30)
 y = np.linspace(ylim[0], ylim[1], 30)
 Y, X = np.meshgrid(y, x)
 xy = np.vstack([X.ravel(), Y.ravel()]).T
 P = model.decision_function(xy).reshape(X.shape)

 # Plot decision boundary and margins
 ax.contour(X, Y, P, colors='k',
            levels=[-1, 0, 1], alpha=0.5,
            linestyles=['--', '-', '--'])

 # Plot support vectors
 if plot_support:
    ax.scatter(model.support_vectors_[:, 0],
        model.support_vectors_[:, 1],
        s=300, linewidth=1, facecolors='none')
 ax.set_xlim(xlim)
 ax.set_ylim(ylim)

# Call the function to show points and SV boundaries
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='winter')
plot_svc_decision_function(model)
plt.show()

# Make predictions (will be array([-1]) or array([1]))
print('predicted')
print(model.predict([[-3, 4]]))
print(model.predict([[7, 5]]))

