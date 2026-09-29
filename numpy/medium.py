import numpy as np


scores = np.array([
    [70,80,90],
    [60,75,85],
    [80,85,95],
    [75,70,80],
])


# Means of the students distinct

print("Averages of the students: ", scores.mean(axis=1))


# Averages of the exams

print("Averages of the exams:",scores.mean(axis=0))

# Students that have mean over 80

print("Students who have mean score above 80",scores[scores.mean(axis=1) > 80])

# Scores that under 70

print("Scores under 70: ",scores[scores < 70])

# Adding 5 to all scores but no one will be higher than 100

scores[scores <= 95] += 5

print(scores)