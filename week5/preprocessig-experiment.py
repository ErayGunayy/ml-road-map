import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

houses = pd.read_csv("pandas/train.csv")

numerical_features = ["OverallQual","GrLivArea","GarageCars","YearBuilt","FullBath"]
categorical_features = ["Neighborhood","KitchenQual","HouseStyle"]


y = houses["SalePrice"]

X_for_model_a = houses[numerical_features]

X_a_train,X_a_val,y_a_train,y_a_val = train_test_split(X_for_model_a,y,test_size=0.2,random_state=1)

model_a = RandomForestRegressor(random_state=1)
model_a.fit(X_a_train,y_a_train)
prediction_a = model_a.predict(X_a_val)
mae_model_a = mean_absolute_error(y_a_val,prediction_a)


########################################################

X_for_model_b = houses[numerical_features + categorical_features]
X_b_train,X_b_val,y_b_train,y_b_val = train_test_split(X_for_model_b,y,random_state=1,test_size=0.2)

my_imputer = SimpleImputer(strategy="most_frequent",missing_values=np.nan)
imputed_X_b_train = pd.DataFrame(my_imputer.fit_transform(X_b_train),columns=X_b_train.columns,index=X_b_train.index)
imputed_X_b_val = pd.DataFrame(my_imputer.transform(X_b_val),columns=X_b_val.columns,index=X_b_val.index)

X_b_train = imputed_X_b_train
X_b_val = imputed_X_b_val





encoder = OneHotEncoder(handle_unknown="ignore",sparse_output=False)
cols_train = pd.DataFrame(encoder.fit_transform(X_b_train[categorical_features]))
cols_val = pd.DataFrame(encoder.transform(X_b_val[categorical_features]))

cols_train.index = X_b_train.index
cols_val.index = X_b_val.index

num_X_train = X_b_train.drop(categorical_features,axis=1)
num_X_val = X_b_val.drop(categorical_features,axis=1)

X_b_train = pd.concat([num_X_train,cols_train],axis=1)
X_b_val = pd.concat([num_X_val,cols_val],axis=1)

X_b_train.columns = X_b_train.columns.astype(str)
X_b_val.columns = X_b_val.columns.astype(str)

model_b = RandomForestRegressor(random_state=1)
model_b.fit(X_b_train,y_b_train)
prediction_b = model_b.predict(X_b_val)
mae_model_b = mean_absolute_error(y_b_val,prediction_b)


print("Mae model a: ",mae_model_a)
print("Mae model b: ",mae_model_b)
