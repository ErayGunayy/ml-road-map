import pandas as pd
import numpy as np


data = {
    "Name": ["Ali", "Ayse", "Mehmet", "Zeynep", "Can", "Ece"],
    "Department": ["CENG", "EE", "CENG", "IE", "CENG", "EE"],
    "Grade": [85, 92, 70, 88, 60, 95],
    "StudyHours": [5, 7, 3, 6, 2, 8],
    "Projects": [3, 4, 2, 5, 1, 4]
}

df = pd.DataFrame(data)


#Her bölümün ortalama StudyHours değerini bul.

print(df.groupby("Department")["StudyHours"].mean())

#En yüksek nota sahip öğrenciyi bul.

print(df.iloc[df["Grade"].argmax()])

#En fazla proje yapan öğrencileri bul.

print(df.iloc[df["Projects"].argmax()])

#StudyHours >= 5 olanların ortalama notuyla < 5 olanları karşılaştır.

print(df[df["StudyHours"] >= 5]["Grade"].mean(),df[df["StudyHours"] < 5]["Grade"].mean())

#Yeni bir kolon oluştur:

def get_performance(grade):
    if grade >= 90:
        return "Excellent"
    elif grade >= 80:
        return "Good"
    elif grade >= 70:
        return "Average"
    else:
        return "Needs Improvement"

df["Performance"] = df["Grade"].apply(get_performance)



def Study_level(study_hours):
    if study_hours >= 7:
        return "High"
    elif study_hours >= 4:
        return "Medium"
    else:
        return "Low"

df["StudyLevel"] = df["StudyHours"].apply(Study_level)

print(df)