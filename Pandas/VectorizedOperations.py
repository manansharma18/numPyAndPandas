import pandas as pd

my_dict = {'a' : 45, 'b' : 35. , 'c' : 'man'}

series = pd.Series(my_dict)
my_dict1 = my_dict.copy()
my_dict1.pop('a')
my_dict1['d'] = 20
series1 = pd.Series(my_dict1)
print(series1+series)