# 1.	Write a Python Program to find sum of array?
import logging
logging.basicConfig(filename = "sum_of_array.log",level = logging.DEBUG, format = "%(levelname)s %(asctime)s %(name)s %(message)s")

def sum_array(l):
    '''This function gives the sum of an array and detects the number of non-integers in the array'''
    k = 0
    n = 0
    for i in l:
        try:
            k = k+i
        except:
            n = n+1
            continue
    logging.info("This array has %s non-intergers", n)
    return k
l1 = [3,4,"ajaja",9.8,5,6,7,8.9,9,"pure"]

logging.info("The sum of an array is %s", sum_array(l1))
