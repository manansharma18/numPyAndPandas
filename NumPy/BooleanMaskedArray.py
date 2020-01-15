import numpy as np

my_vector = np.arange(5,50,6)
my_new_vector = my_vector % 7
print(my_new_vector)
booleanValue = 0 == (my_vector % 7)
print(booleanValue)

print(np.logical_and(my_new_vector, booleanValue))
