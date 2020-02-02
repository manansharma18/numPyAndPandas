import numpy as np
import pandas as pd


my_dict = {'a': [3,4,5,6], 'b' : [22,3,3,4],'c' : ['hike', 4,5,6]}

dataFrame = pd.DataFrame(my_dict)

# print(dataFrame)

index = [0,1,2,3]

dataFrame = pd.DataFrame(my_dict, index = index)

#print(dataFrame)

seriesDict = {'one' : pd.Series([1,2,3] , index = ['a','b','c']),
'two': pd.Series([1,2,3,4] , index = ['a','b','c','d'])}
dataFrame2 = pd.DataFrame(seriesDict)

#print(dataFrame['c'])
print(dataFrame)

print(dataFrame2)

dataFrame2['one'] = ['a', 1, 2,3]
print(dataFrame2)