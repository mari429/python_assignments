# 4.	Write a Python program to convert key-values list to flat dictionary?
original_dict = {'name': ['Jan', 'Feb', 'March'], 'month': [1, 2, 3]}
flat_dict = {}
for v in range(len(original_dict['name'])):
    flat_dict.update({original_dict['month'][v]:original_dict['name'][v]})
print (flat_dict)