import datetime 
from pandas_datareader import data , wb
import matplotlib.pyplot as plt


startTime = datetime.datetime(2010,1,1)
endTime = datetime.datetime(2016,7,15)

yahoo = data.DataReader("F","yahoo",startTime,endTime)

yahoo.plot()
plt.show()