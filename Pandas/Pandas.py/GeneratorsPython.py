sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares


print(sq_list)
print(sq_iterator)

try: 
    x = 5/0
except ZeroDivisionError:
    print('Cannot divide by zero')
finally:
    print("lolz")