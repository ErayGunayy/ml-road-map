import pandas as pd 
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer



houses = pd.read_csv("pandas/train.csv")

categorical_features = ["Neighborhood","KitchenQual","HouseStyle"]
numerical_features = ["OverallQual","GrLivArea","GarageCars","YearBuilt","FullBath"]

X = houses[categorical_features+numerical_features]
y = houses["SalePrice"]

X_train,X_val,y_train,y_val = train_test_split(X,y,test_size=0.2,random_state=0)

numerical_transformer = SimpleImputer(strategy="median")

categorical_transformer = Pipeline(steps=[
    ("imputer",SimpleImputer(strategy="most_frequent")),
    ("onehot",OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num",numerical_transformer,numerical_features),
        ("cat",categorical_transformer,categorical_features)
    ]
)

model = RandomForestRegressor(random_state=1,n_estimators=100)

my_pipeline = Pipeline(steps=[
    ("preprocessor",preprocessor),
    ("model",model)
])

my_pipeline.fit(X_train,y_train)
preds = my_pipeline.predict(X_val)

score = mean_absolute_error(y_val,preds)

print("MAE: ",score)