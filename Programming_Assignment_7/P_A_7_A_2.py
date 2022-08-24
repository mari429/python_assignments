# 2.	Write a Python Program to find largest element in an array?
import logging
logging.basicConfig(filename="largest_in_array.log",level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')
def large_element_array(l):
    '''This function gives the largest element in an array'''
    k = 0
    n = 0
    for i in range(len(l)):
        try:
            if k < l[i]:
                k = l[i]
            else:
                continue
        except:
            n = n+1
            continue
    logging.info("This array has %s non-intergers in it", n)
    return k
l1 = [27, 29, 45, 3, 4, 98, 56, 54, 'kushi', 84, 5, 6, 'Hashinee', 8, 9, 34]
m = large_element_array(l1)
logging.info ("The largest number in the array is %s", m)