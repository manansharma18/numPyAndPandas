import pandas as pd
import numpy as np


dataFrame = pd.DataFrame(np.array(np.random.rand(36).reshape(6,6)))
missing = np.NaN
#print(dataFrame)

dataFrame.iloc[1:5,2:5] = missing

newdataFrame= dataFrame.fillna({0 : 1, 1: 2 , 2:3,3:2, 4: 5})
print(newdataFrame)
print(dataFrame)
print(dataFrame.isnull().sum())
print(dataFrame.dropna())
print(dataFrame.dropna(axis = 1))