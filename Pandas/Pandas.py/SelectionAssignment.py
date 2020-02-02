import pandas as pd
import numpy as np

try: 

    data = np.array(np.arange(25).reshape(5,5))

    index = pd.date_range('20200201', periods=5)

    dataFrame = pd.DataFrame(data, index = index, columns = list('ABCDE'))

    dataFrameCopy = dataFrame.copy()
 

    #print(dataFrame[0:2])
    #print(dataFrame['D']['2020-02-04'])
    #print(dataFrame['2020-02-02':'2020-02-05'])
    #print(dataFrame['B'])
    #print(dataFrame.loc[index[1:3]])
    #print(dataFrame.loc[:,['B','D']])
    #print(dataFrame.loc[index[1:3],['E','A']])
    #print(dataFrame.loc['2020-02-03',['B','D']][1])
    #print(dataFrame.iloc[[0,1,3],[0,2]])
    #print(dataFrame.iloc[1:3,0:2])
    
    dataFrameCopy['Fruits'] =['apple','orange','banana','avocado','mango']
    #print(dataFrameCopy)
    #print(dataFrameCopy[dataFrameCopy['Fruits'].isin(['banana','mango'])])
    #print(dataFrameCopy['Fruits'][1])
    dataFrameCopy.at[index[3],'Fruits'] = 'Pear'
    dataFrameCopy.iat[2,5] = 'Muskmellon'
    print(dataFrameCopy)
    #print(dataFrame)

except Exception as e : 
    print('The date is out of range', format(e))

