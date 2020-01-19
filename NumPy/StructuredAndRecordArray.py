import numpy as np

person_data_def = [('name','S6'),('height','f8'),
('weight','f8'),('age','i8')]

print(person_data_def)

newArray = np.zeros(4,dtype=person_data_def)

newArray[0] = ('Alpha',34,56,9)
newArray[1] = ('Beta',87,60,18)
newArray[2] = ('Charlie',97,70,12)

print("Age is ",+newArray['age'])
print("Age is ",+newArray['age'][2])
#converts interger age to float
print("Age /2 is ",newArray['age']/2)

print(newArray)
print(newArray[0:])

newMutiDimenArray = np.zeros((4,3,2),dtype=person_data_def)

print(newMutiDimenArray)
newMutiDimenArray[1][1][1] = ('Beta',87,60,18)
print(newMutiDimenArray)
print(newMutiDimenArray[['height','age']])


#Record Array

recordArray = np.rec.array([('Charlie',97,70,12),('Beta',87,60,18)]
,dtype=person_data_def)

print(recordArray)
print(recordArray[1].age)