import pandas as pd
import numpy as np


dataFrame = pd.DataFrame(np.arange(25).reshape(5,5))
dataFrame1 = pd.DataFrame(np.arange(30).reshape(6,5))

ConcatDF = pd.concat([dataFrame,dataFrame1])

ConcatDF1 = pd.concat([dataFrame,dataFrame1], axis = 1 )

print(ConcatDF)
print(ConcatDF1)


print(dataFrame.drop([0,2]))
print(dataFrame1.drop([0,2], axis = 1))

seriesObj = pd.Series(np.arange(6))
seriesObj.name = 'addedVariable'

newDf = pd.DataFrame.join(dataFrame,seriesObj)
print(newDf)

apendedDataFrame = newDf.append(ConcatDF,ignore_index=False)
apendedDataFrame1 = newDf.append(ConcatDF,ignore_index=True)

print(apendedDataFrame)
print(apendedDataFrame1)
