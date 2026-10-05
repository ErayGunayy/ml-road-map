from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd



data = pd.read_csv("pandas/train.csv")

features = ["LotArea","YearBuilt","1stFlrSF","2ndFlrSF","FullBath","BedroomAbvGr","TotRmsAbvGrd","OverallQual","GrLivArea"]

X = data[features]
y = data["SalePrice"]


X_train,X_val,y_train,y_val = train_test_split(X,y,train_size=0.2,random_state=1)


model = RandomForestRegressor(random_state=1)

model.fit(X_train,y_train)

pred_val = model.predict(X_val)

mae = mean_absolute_error(y_val,pred_val)

importence = pd.Series(model.feature_importances_,index=features)

print(importence.sort_values(ascending=False))
## Normal decisiontreeregressora kıyasla max_leaf_node=100 iken aradaki fark 1k daha az

## Tree sayısı arttıkça başta azaldı ama azalma miktarı o kadar da çok değil hatta bence bir şeyi etkilemiyor çünkü verdiğim en büyük değerde mae daha az geldi diğerlerine kıyasla
