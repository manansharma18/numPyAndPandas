import numpy as np

leftMatrix = np.arange(6).reshape(2,3)
rightMatrix = np.arange(15).reshape(3,5)

newMatrix = np.dot(leftMatrix,rightMatrix)

print(newMatrix)

