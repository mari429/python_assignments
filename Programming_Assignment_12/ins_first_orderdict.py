# 5.	Write a Python program to insertion at the beginning in OrderedDict?
from collections import OrderedDict
dict1 = OrderedDict([('Hardhik',72),('Rohith',67),('Jadeja',90)])
dict1.update({'Kholi': 108})
dict1.move_to_end('Kholi',last=False)
print ("The resultant dictionary after inserting is :", dict1)