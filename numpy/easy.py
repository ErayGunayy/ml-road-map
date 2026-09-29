import numpy as np



scores = np.array([
    [70,80,90],
    [60,75,85],
    [80,85,95],
    [75,70,80],
])


# shape

print("Shape of the scores array:",scores.shape)


# scores of the first student


print("Scores of the first student:",scores[0])


# second notes of the students

print("Second notes of the students: ", scores[:,1])

#mean

print("Average of the scores",scores.mean())

# max , min

print("Max score and min score: ",scores.max(),scores.min())