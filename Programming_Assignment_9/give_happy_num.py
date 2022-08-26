# 4.	Write a Python program to print all happy numbers between 1 and 100?
c= []
for num in range(100):
    a = num
    while len(str(a)) != 1:
        b = 0
        for i in str(a):
            b = b + (int(i) ** 2)
        a = b
    if a == 1:
        c.append(num)
    else:
        continue
print(c)