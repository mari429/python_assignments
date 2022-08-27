# 8.	Write a Python program to print odd numbers in a List?
a = [*range(1,31)]
for i in a:
    if i%2 != 0:
        print(i)