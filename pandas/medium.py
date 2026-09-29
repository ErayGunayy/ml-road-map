import pandas as pd

data = {
    "Name": ["Ali", "Ayse", "Mehmet", "Zeynep", "Can", "Ece"],
    "Department": ["CENG", "EE", "CENG", "IE", "CENG", "EE"],
    "Grade": [85, 92, 70, 88, 60, 95],
    "StudyHours": [5, 7, 3, 6, 2, 8],
    "Projects": [3, 4, 2, 5, 1, 4]
}

df = pd.DataFrame(data)


#Notu 80 üzerindeki öğrencileri getir.

print(df[df["Grade"] > 80])

#CENG öğrencilerini getir.

print(df[df["Department"] == "CENG"])

#CENG olup notu 70 üzerinde olan öğrencileri getir.

print(df[(df["Department"] == "CENG") & (df["Grade"] > 70)])

#Öğrencileri Grade değerine göre büyükten küçüğe sırala.

print(df.sort_values("Grade",ascending=False))

#Her bölümün ortalama notunu bul.

print(df.groupby("Department")["Grade"].mean())