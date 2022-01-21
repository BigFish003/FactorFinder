import time
import random
import math
factors_for_number = []
print("this finds prime factors for numbers")
number = input("enter your integer")
number = int(number)
index = 2
for i in range(number):
    factor = number/index
    if factor.is_integer():
        factors_for_number.append(index)
        index += 1
    else:
        index += 1
print(factors_for_number)