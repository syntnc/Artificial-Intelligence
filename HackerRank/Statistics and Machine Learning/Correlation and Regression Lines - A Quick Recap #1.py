import numpy as np
from scipy.stats import pearsonr

X = np.array([15, 12, 8, 8, 7, 7, 7, 6, 5, 3])
Y = np.array([10, 25, 17, 11, 13, 17, 20, 13, 9, 15])

print(round(pearsonr(X, Y)[0], 3))
