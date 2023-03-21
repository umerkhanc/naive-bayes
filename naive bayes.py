import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = [0, 0, 1, 1]

clf = GaussianNB()
clf.fit(
