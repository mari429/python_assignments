# 2.	Write a Python program to find the sum of all items in a dictionary?
dict1 = {'hdgdh':5454, 'dhdjdh':7373, 636:9898, 'shshd':8733, 3737: 'skssh'}
sum_all_dict =  0
for k,v in dict1.items():
    if type(k) == int:
        sum_all_dict+=k
    if type(v) == int:
        sum_all_dict+=v
    else:
        continue
print (sum_all_dict)