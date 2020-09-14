from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data  # we only take the first two features.
y = iris.target

# Train a Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X, y)

# Save the model as a pkl file
filename = 'ml_model/iris_model.pkl'
pickle.dump(clf, open(filename, 'wb'))
