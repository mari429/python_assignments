# 7.	Write a Python program to sort Python Dictionaries by Key or Value?
from collections import OrderedDict
dict1 = {'vishal':'safety', 'manu':'environment', 'kannan':'health', 'vishnu': 'quality', 'rathish':'admin', 'biju': 'head'}
l1 = []
for i in dict1.keys():
    l1.append(i)
dict2 = OrderedDict([])
for j in range(len(sorted(l1))):
    dict2.update({sorted(l1)[j]:dict1[sorted(l1)[j]]})
print(f'The dictionary sorted by keys is {dict2}')
l2 = []
for k in dict1.values():
    l2.append(k)
dict3 = OrderedDict([])
l3 = sorted(l2)
for n in range(len(l3)):
    for m in dict1.keys():
        if dict1[m] == l3[n]:
            dict3.update({m:l3[n]})

print(f'The dictionary sorted by values is {dict3}')