import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
dataset = pd.read_csv("melb_data.csv")
dataset.head()

dataset=dataset.drop('Unnamed: 0', axis=1)
dataset.columns

dataset = dataset[["Rooms", "Price", "Bedroom2", "Bathroom","Landsize", "BuildingArea", "YearBuilt"]]
dataset.isna().sum()


dataset = dataset.dropna()
dataset['HouseAge'] = 2022 - dataset["YearBuilt"].astype(int)
dataset = dataset.drop("YearBuilt", axis=1)
dataset.head()

def normalize(df):
result = df.copy()
for feature_name in df.columns:
max_value = df[feature_name].max()
min_value = df[feature_name].min()
result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
return result


train, test = train_test_split(df, test_size=0.3)
train_y = train[["Price"]]
train_x = train.drop(["Price"], axis=1)
test_y = test[["Price"]]
test_x = test.drop(["Price"], axis=1)


model = LinearRegression()
model.fit(train_x, train_y)
predictions = model.predict(test_x)
predictions
mean_absolute_error(predictions, test_y)
