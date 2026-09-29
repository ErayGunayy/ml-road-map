import pandas as pd




train = pd.read_csv("pandas/train.csv")


#Dataset kaç row × column?

print(train.shape)

#İlk 10 satırı göster.

print(train.head(10))

#SalePrice ortalaması nedir?

print(train["SalePrice"].mean())

#En pahalı ev kaç dolar?

print(train["SalePrice"].max())

#En ucuz ev kaç dolar?

print(train["SalePrice"].min())

#Hangi kolonlarda missing value var?

print(train.isna())

#En fazla missing value olan 10 kolonu bul.

print(train.isna().sum().sort_values(ascending=False)[:10])

#OverallQual değerine göre ortalama SalePrice hesapla.

print(train.groupby("OverallQual")["SalePrice"].mean())

#Neighborhood'a göre ortalama SalePrice hesapla ve pahalıdan ucuza sırala.

print(train.groupby("Neighborhood")["SalePrice"].mean().sort_values(ascending=False))

#YearBuilt >= 2000 olan evlerin ortalama fiyatıyla < 2000 olanları karşılaştır.

print(train[train["YearBuilt"] >= 2000]["SalePrice"].mean())
print(train[train["YearBuilt"] < 2000]["SalePrice"].mean())
