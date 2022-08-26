# 6.	Write a Python program to print all pronic numbers between 1 and 100?
pronic = []
for i in range(1,101):
    for j in range(1,i):
        if j*(j-1) == i:
            pronic.append(i)
print (pronic)
