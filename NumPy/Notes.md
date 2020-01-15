*In Numpy every element in the list is of same type. So every element of the list was converted to the last element of the list. Integer value were converted to complex data type*

my_tuple = (14 ,4.56, 5+7j)

print( np.array(my_tuple))

[14.  +0.j  4.56+0.j  5.  +7.j]

### Difference between python and numpy data structure. Below is the example of OOPS in python and numpy. 

my_tuple * 6 in python will replicate the entire array 6 times. 
np.array(my_tuple)*6 will multiply each element of the tuple with 6. 
