import pandas as pd

data = {
    "Name": ["Ali", "Ayse", "Mehmet", "Zeynep", "Can", "Ece"],
    "Department": ["CENG", "EE", "CENG", "IE", "CENG", "EE"],
    "Grade": [85, 92, 70, 88, 60, 95],
    "StudyHours": [5, 7, 3, 6, 2, 8],
    "Projects": [3, 4, 2, 5, 1, 4]
}

df = pd.DataFrame(data)

#İlk 3 satırı göster.

print("First 3 row: ",df.head(3))

#DataFrame'in boyutunu bul.

print("The shape of the df", df.shape)

#Sadece Name kolonunu getir.

print(df.loc[:,"Name"])

#Name ve Grade kolonlarını getir.

print(df.loc[:,["Name","Grade"]])

#Ortalama notu bul.

print(df["Grade"].mean())