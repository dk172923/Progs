import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree

# Read the dataset
dataset = pd.read_csv("Maternal Health Risk Data Set.csv")

# Preprocess the data
dataset['RiskLevel'] = dataset['RiskLevel'].replace('low risk', 0).replace('mid risk', 1).replace('high risk', 2)
y = dataset['RiskLevel']
X = dataset.drop(['RiskLevel'], axis=1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a random forest classifier
rfc = RandomForestClassifier(n_estimators=2, max_depth=2, random_state=42)
rfc.fit(X_train, y_train)

# Visualize each decision tree in the random forest
features = X.columns.values
classes = ['0', '1', '2']
for i in rfc.estimators_:
    plt.figure(figsize=(12, 6))
    tree.plot_tree(i, feature_names=features, class_names=classes, fontsize=8, filled=True, rounded=True)
    plt.show()
