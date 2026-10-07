import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = pd.DataFrame({
    "City": [
        "Ankara",
        "Istanbul",
        "Ankara",
        "Izmir",
        "Istanbul"
    ]
})

categorical_cols = data.select_dtypes("object").columns

encoder = OneHotEncoder(sparse_output=False)
encoded_data = encoder.fit_transform(data[categorical_cols])
encoded_df = pd.DataFrame(encoded_data,columns=encoder.get_feature_names_out(categorical_cols))

final_df = pd.concat([data.drop(columns=categorical_cols),encoded_df],axis=1)

print("One hot encoded data: ")
print(final_df)