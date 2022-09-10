# 6.	Write a Python program to check order of character in string using OrderedDict()?
from collections import OrderedDict
original_string = "data scientist"
pattern_string = "dci"
dict1 = OrderedDict.fromkeys(original_string)
# print(dict1)
order_string = 0
for k,v in dict1.items():
    if k == pattern_string[order_string]:
        order_string = order_string + 1
        if order_string == len(pattern_string):
            print(f"Order of the string '{pattern_string}' is correct in '{original_string}'")
            break
else:
    print(f"Order of the string '{pattern_string}' is not correct in '{original_string}'")
