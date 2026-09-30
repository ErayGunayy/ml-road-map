import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

def get_mae(max_leaf_node,X_train,X_val,y_train,y_val):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_node,random_state=1)
    model.fit(X_train,y_train)
    prediction = model.predict(X_val)
    return mean_absolute_error(y_val,prediction)

def calculate_custom_mae(y_true,y_pred):
    total = 0
    number_of_data = y_true.shape[0]
    for i in range(number_of_data):
        total += abs(y_true.iloc[i] - y_pred[i])

    return total / (number_of_data)

housePrice = pd.read_csv("pandas/train.csv")


features = ["LotArea","YearBuilt","1stFlrSF","2ndFlrSF","FullBath","BedroomAbvGr","TotRmsAbvGrd","OverallQual","GrLivArea"]

X = housePrice[features]

y = housePrice["SalePrice"]

X_train,X_val,y_train,y_val = train_test_split(X,y,test_size=0.2,random_state=42)


salePriceModel = DecisionTreeRegressor(random_state=1,max_leaf_nodes=100)

salePriceModel.fit(X_train,y_train)

train_prediction = salePriceModel.predict(X_train)
val_prediction = salePriceModel.predict(X_val)

train_MAE = mean_absolute_error(y_train,train_prediction)
val_MAE = mean_absolute_error(y_val,val_prediction)
val_custom_MAE = calculate_custom_mae(y_val,val_prediction)

for leaf in [5,25,50,100,250,500]:
    print(get_mae(leaf,X_train,X_val,y_train,y_val))

print(val_MAE,train_MAE)







