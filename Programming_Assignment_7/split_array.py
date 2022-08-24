# 4.	Write a Python Program to Split the array and add the first part to the end?
def split_array(l,n):
    l2 = l[n:len(l)] + l[0:n]
    return l2

l1 = ["ksjdh", 6878, 2726, "dbiebkj", 3636, "sabhsdg", 26252, 98282, 2929]
n1 = int(input("Enter the number of items to split in the array?"))

print (split_array(l1,n1))