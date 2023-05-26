import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Read the dataset
df = pd.read_csv("C:\\Users\\dhine\\Downloads\\Telco-Customer-Churn.csv")

# Drop unwanted features
#df = df.drop(['Unnamed: 0'], axis=1)

# Convert categorical variables to numerical using LabelEncoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

# Split the data into features (X) and target variable (y)
X = df.drop('Churn', axis=1)
y = df['Churn']

# Create the decision tree classifier
dt = DecisionTreeClassifier(max_depth=2, random_state=43)
dt.fit(X, y)

# Visualize the decision tree using matplotlib
plt.figure(figsize=(10, 10))
_ = plot_tree(dt, feature_names=X.columns, class_names=['Not Churn', 'Churn'], filled=True)
plt.show()
