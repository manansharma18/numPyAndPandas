import numpy as np


#print(np.__version__)

list = np.arange(10)
newList = np.array([],dtype='int32')
#print(list)

for i in reversed(list):
  newList =  np.append(newList,i)
#print("Reversed list is ",newList)


#print("Tripled list is ", newList*3)

zeros = np.zeros(20, dtype = 'int32')
zeros[::5] = 4

#print(zeros)

preTransposeArray = np.arange(15).reshape(3,5)

#print(preTransposeArray)
postTransposeArray = preTransposeArray.T

#print(postTransposeArray)

identityMatrix = np.identity(5,dtype='int32')

#print(identityMatrix)

#print(np.asmatrix(np.eye(5),dtype ='int'))

meanArray = np.random.rand(30)

mean = np.mean(meanArray)

#print(mean)

#print(meanArray.mean())
unSortedArray = np.random.rand(20)
sortedArray = np.sort(unSortedArray)
#print(unSortedArray)
#print(sortedArray)
sortedArray[-1] = 1234
#print(sortedArray)
unSortedArray[np.argmax(unSortedArray)] = 1234
#print(unSortedArray)
camelot_dtype = [('name','S10'),('height',float),('age',int)]
camelot_values = [('Alpha',34,9),('Beta',60,18),('Charlie',97,70)]

camelot_array = np.array(camelot_values,dtype=camelot_dtype)
sortedCamelotArray = np.sort(camelot_array, order= 'height')
#print(sortedCamelotArray['height'][sortedCamelotArray.size -1])
#for n in np.arange(sortedCamelotArray.size):
  #print(sortedCamelotArray[n])

immutableArray = np.array(np.arange(12))
immutableArray.flags.writeable = False
#immutableArray[0] = 1234

array_3_3 = np.arange(18).reshape(3,6)
for index , value in np.ndenumerate(array_3_3):
  print(index, value)