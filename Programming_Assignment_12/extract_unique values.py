# 1.	Write a Python program to Extract Unique values dictionary values?
test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}
l= []
for i in test_dict.values():
    for j in i:
        l.append(j)
print (list(set(l)))
