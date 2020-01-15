* NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

At the core of the NumPy package, is the ndarray object.*

*In Numpy every element in the list is of same type. So every element of the list was converted to the last element of the list. Integer value were converted to complex data type*

my_tuple = (14 ,4.56, 5+7j)

print( np.array(my_tuple))

[14.  +0.j  4.56+0.j  5.  +7.j]

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