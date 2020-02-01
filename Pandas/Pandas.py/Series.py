import pandas as pd
import numpy as np

#series = pd.Series([1,2,3,5,5])
#print(series)

dataRange = pd.date_range('20200201',periods =6)
print(dataRange)
data = np.array(np.arange(24).reshape(6,4))

dataFrame = pd.DataFrame(data, index = dataRange,columns = list("aBCd"))

print(dataFrame)

dictionaryDataFrame = pd.DataFrame({
    "Float" : 1.,
    "time"  : pd.date_range('20200201', periods=4),
    "series" : pd.Series([1,2,3,4]),
    "categories" : pd.Categorical(['Time','Test','Technology','Traction']),
    "dull" : "boring"
})

print(dictionaryDataFrame)