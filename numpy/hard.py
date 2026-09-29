import numpy as np



sales = np.array([
    [120, 150, 170, 200],
    [80,  90,  110, 130],
    [200, 210, 190, 250],
    [50,  70,  65,  90]
])


# Shop that have the most sales

print("Shop that have the most average: ",sales[sales.sum(axis=1).argmax()])

# Month that have the most average

print("Month that have the most average: ",sales[:,sales.mean(axis=0).argmax()])

# Total sales of every shop

print("Total sales of every shop: ",sales.sum(axis=1))

# Sales higher than 150

print("Sales higher than 150: ",sales[sales > 150])

# Shops that have sales which are higher than the general average

gen_avg = sales.mean()
print("Shops that have sales which are higher than the general average: ", sales[sales.mean(axis=1) > gen_avg])