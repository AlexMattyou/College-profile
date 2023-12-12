import numpy as np

x = np.array([[4, 4], [5, 4], [6, 5], [1, 1], [2, 1], [3, 2]])
y = np.array([0, 0, 0, 1, 1, 1])

class0 = x[y == 0]
class1 = x[y == 1]

mean0 = class0.mean(axis=0)
var0 = class0.var(axis=0)
mean1 = class1.mean(axis=0)
var1 = class1.var(axis=0)

def gaussian(x, mean, var):
    return (1 / np.sqrt(2 * np.pi * var)) * np.exp(-(x - mean) ** 2 / (2 * var))

prob0 = len(class0) / len(x)
prob1 = len(class1) / len(x)

def predict(x):
    prod0 = gaussian(x, mean0, var0).prod() * prob0
    prod1 = gaussian(x, mean1, var1).prod() * prob1
    return 0 if prod0 > prod1 else 1

newX = np.array([2.5, 1.5])
print("Predicted class:", predict(newX))

newX = np.array([4.5, 4.5])
print("Predicted class:", predict(newX))

