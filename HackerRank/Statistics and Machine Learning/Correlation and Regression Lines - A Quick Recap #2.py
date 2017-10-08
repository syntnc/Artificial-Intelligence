import numpy as np 
X = np.array([15, 12, 8, 8, 7, 7, 7, 6, 5, 3])
Y = np.array([10, 25, 17, 11, 13, 17, 20, 13, 9, 15])
slope_of_reregression = float(len(X) * sum(X * Y) - sum(X) * sum(Y)) / (len(X) * sum(X ** 2) - sum(X) ** 2)
print(round(slope_of_reregression, 3))
