# 3.	Write a Python Program for array rotation?
import logging
logging.basicConfig(filename = "array_rotation.log", level = logging.INFO, format = '%(levelname)s %(asctime)s %(name)s %(message)s')
l = [3,4,5,6,7,8,9,34,27,29,45]
k = []
i = 8
while len(k) != len(l):
    k.append(l[i])
    i=i+1
    if i == len(l):
        i=0
logging.info ("The rotated array is %s", k)


