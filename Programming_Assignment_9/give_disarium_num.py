# 2.	Write a Python program to print all disarium numbers between 1 to 100?
c=[]
for a in range(100):
    b = 0
    for i in str(a):
        b = b + (int(i) ** (int(str(a).index(i)) + 1))
    if b == a:
        c.append(a)
print(c)
