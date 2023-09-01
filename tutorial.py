"""
Reduce Function -> Applies a function to all elements in a list and 
    returns the final value, used to compute a final value 
This makes it different from map, because we are not just iterating over
    the list but actually computing and returning a value
This can be done super easily with lambdas (an anonymous function)

functools are a way to import higher order functions in python -> 
    Higher order functions act on or return another function
"""

import functools

values = [10,1,2,3,4,5]

# add values in a list
def add(a, b):
    return a + b

# add values in a list
# print(functools.reduce(add, values))
# print(functools.reduce(lambda a,b:a+b, values))

# get smallest value in a list
# print(functools.reduce(lambda a,b: a if a < b else b, values))

# reduce with an initializer
print(functools.reduce(lambda a, b: a+b, values, 100))