# 7.	Write a Python program to print even numbers in a list?
a = [*range(1,31)]
for i in a:
    if i%2 == 0:
        print(i)