# 3.	Write a Python program to Merging two Dictionaries?
def merge_dict(dict1,dict2):
    dict1.update(dict2)
    return dict1

dict_pers = {'name': 'Mari Sankar', 'age' : 35, 'education' : 'graduate'}
dict_prof = {'profession' : 'data scientist', 'city': 'bangalore'}
merged_dict = merge_dict(dict_pers,dict_prof)
print(merged_dict)
