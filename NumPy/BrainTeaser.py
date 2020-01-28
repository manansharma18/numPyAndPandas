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

print(np.asmatrix(np.eye(5),dtype ='int'))