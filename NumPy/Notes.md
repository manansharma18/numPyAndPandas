* NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

At the core of the NumPy package, is the ndarray object.*

*In Numpy every element in the list is of same type. So every element of the list was converted to the last element of the list. Integer value were converted to complex data type*

my_tuple = (14 ,4.56, 5+7j)

print( np.array(my_tuple))

[14.  +0.j  4.56+0.j  5.  +7.j]
my_array = np.array(my_tuple)
my_array[-2] : 4.56+0.j
my_array[::2] (start:stop:step )// every second element
### Difference between python and numpy data structure. Below is the example of OOPS in python and numpy. 

my_tuple * 6 in python will replicate the entire array 6 times. 
np.array(my_tuple)*6 will multiply each element of the tuple with 6. 

## Difference in Python and NumPy
NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original.
The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory. The exception: one can have arrays of (Python, including NumPy) objects, thereby allowing for arrays of different sized elements.
NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences.
A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays. In other words, in order to efficiently use much (perhaps even most) of today’s scientific/mathematical Python-based software, just knowing how to use Python’s built-in sequence types is insufficient - one also needs to know how to use NumPy arrays.

## Why is NumPy fast?
Vectorization describes the absence of any explicit looping, indexing, etc., in the code - these things are taking place, of course, just “behind the scenes” in optimized, pre-compiled C code. Vectorized code has many advantages, among which are:

1. vectorized code is more concise and easier to read
2. fewer lines of code generally means fewer bugs the code more closely resembles standard mathematical notation (making it easier, typically, to correctly code mathematical constructs)
3. vectorization results in more “Pythonic” code. Without vectorization, our code would be littered with inefficient and difficult to read for loops.

## NumPy Arange function
It creates evently spaced values within the given interval. (start, stop]. Stop value is compulsory 
np.arange(5,10) : [5 6 7 8 9]
my_vector = np.arange(35)
my_vector.size(7,5) : converts array to a 7 * 5 matrix
np.arange(5,0): []// Does not work in reverse order
np. arange(5,50,5) : [ 5 10 15 20 25 30 35 40 45]
np.arange(50, step = 5) : [ 0  5 10 15 20 25 30 35 40 45]

## Numpy Linspace,

Unline Arange function the linspace function includes the stop value while reacting interval. The default return type of zero() and one() is float type value. 

print(np.zeros(5))
print(np.ones((4,5)))
print(np.linspace(5,90,3))

[0. 0. 0. 0. 0.]
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
[ 5.  47.5 90. ]

## BroadCasting.py 
The term broadcasting describes how numpy treats arrays with different shapes during arithmetic operations. Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes. The size of both arrays must be same. But we can add an array of integers with an array of floats. Provided both have same number of elements in the array.

ndim :  my_vector.for dimensions
shape : my_vector.shape
size :  my_vector.size
dtype : my_vector.dtype
np.inner(matrix1, matrix2): inner product of 2 matrices. But, both should be 1 D matrix
np.dot(matrix1, matrix2): multiply any sized matrix

leftMatrix = np.arange(6).reshape(2,3)
rightMatrix = np.arange(15).reshape(3,5)

newMatrix = np.dot(leftMatrix,rightMatrix)

print(newMatrix)
[[ 25  28  31  34  37]
 [ 70  82  94 106 118]]

 numPy .sum() function returns float. Usual python operations return interger

 ## Array

 Same memory space is allocated to each element. Array[0:] : will show information from the first element to the last element. 

 Record array make accessible attributes of an array like Object Oriented Programing.

 ## matplot library

Is a python 2D plotting library for publicasion quality plots. Numbering starts form 1 and not 0. Explode function in pie chart tells that that piece will be separated from the pie chart. 

this means that 2 second piece will be detached from the pie chart
explode = (0,0.1,0)

## Copy and views

Copy copies data from one location and creates another another reference for the new variable. Views create a new variable but with the same reference to the original variable. 

NumPy slicing creates a view instead of a copy as in the case of builtin Python sequences such as string, tuple and list. Care must be taken when extracting a small portion from a large array which becomes useless after the extraction, because the small portion extracted contains a reference to the large original array whose memory will not be released until all arrays derived from it are garbage-collected. In such cases an explicit copy() is recommended.

tree_house = np.array([5,10,32,-9])
dog_house = np.copy(tree_house)
dog_house[0] = 4
// Memory space
dog_house is tree_house : false
dog_house == tree_house : [False, true,true,true]


mi_casa =  np.array([5,10,32,-9])
su_casa = mi_casa

mi_casa is su_casa : true
id(mi_casa) == id(su_casa) : true
mi_casa == su_casa :[True, true,true,true]

mi_casa[2] = 30 : this will change the valie in su_casa as well because they have same reference

## Atributes of array
a = np.array(np.arange(24)).reshape(2,3,4)
ndim: 3
shape: (2,3,4)
size: Size of the array
dtype: int32
itemsize : 4 bytes in 32 bit integer
type(a): numpy.ndarray
append: b= np.append(a,[5,6,7,8]) // b is 1D array with 28 elements
diag : Selects value along the diagonal of the array
np.diag(a, k=1) //selects the diagonal above the main diagonal.
np.diag(x , k=-1) //selects diagonal below the main diagonal. by default k = 0 thats why it selects the main diagonal
unique: selects unique value from the array
c = np.array(np.arange(24)).reshape(2,3,4) *10 +3

np.append(a,c,axis =0) //  appends c at the end of a. New array is (4,3,4) 
axis = 1 is (2,6,4) array
axis = 2 is (2,3,8) array

np.hstack(a,c)// this eliminates the axis parameter and creates copies and not views.

numpy's insert and delete create a new array with new data. 
np.delete(c,1,axis = 0) // Deletes 1 matrix
np.delete(c,1,axis = 1) // Deletes 2nd row as the index is 1
np.delete(c,1,axis = 2) // Deletes 2nd column  as the index is 1

reshape function creates a view of the data and not a copy of data.
ravel() converts a n dim array to 1 dim array
flat return iterator. can be used in loop
fliplr: left right
flipud : up down flip
np.roll(array,5): moves last 5 element to first place
np.roll(array,-5): moves first 5 element to last place

We can also sort ndarrays in NumPy. We will learn how to use the np.sort() function to sort rank 1 and rank 2 ndarrays in different ways. Like with other functions we saw before, the sort function can also be used as a method. However, there is a big difference on how the data is stored in memory in this case. When np.sort() is used as a function, it sorts the ndrrays out of place, meaning, that it doesn't change the original ndarray being sorted. However, when you use sort as a method, ndarray.sort() sorts the ndarray in place, meaning, that the original array will be changed to the sorted one. 

a = np.array([5,6,5,6,4,3,2,8,9])

print(a)
// does not change the array a
print(np.sort(a))
print (a)
print(a.sort())
print(a)
// Output 
[5 6 5 6 4 3 2 8 9]
[2 3 4 5 5 6 6 8 9]
[5 6 5 6 4 3 2 8 9]
None
[2 3 4 5 5 6 6 8 9]
## Universal function

Vectorized wrapper for a python function which has a fixed number of scalar inputs and scalar outputs. 
def truncated_binomial (x):
    return (x+1)**3 - (x)**3 
np.matrix function return value in matrix style. it accepts array like value.

## SymPy library

diff(): for differentiation

numpy.random.random is actually an alias for numpy.random.random_sample. I'll use the latter in the following. (See this question and answer for more aliases.)

Both functions generate samples from the uniform distribution on [0, 1). The only difference is in how the arguments are handled. With numpy.random.rand, the length of each dimension of the output array is a separate argument. With numpy.random.random_sample, the shape argument is a single tuple.

For example, to create an array of samples with shape (3, 5), you can write

sample = np.random.rand(3, 5)
or

sample = np.random.random_sample((3, 5))