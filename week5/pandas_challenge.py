import pandas as pd


data = pd.read_csv("pandas/train.csv")

object_cols = data.select_dtypes("object").columns
numerical_cols = data.select_dtypes(include=["int64","float64"])


print("Categorical columns : ",object_cols)

print("Numerical columns : ",numerical_cols)


max_unique = 0
max_col = ""



for col in object_cols:
    if data[col].nunique() > max_unique:
        max_col = col
        max_unique = data[col].unique().shape[0]

print(max_col,max_unique)