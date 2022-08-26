num = 28
a = num
while len(str(a)) != 1:
    b = 0
    for i in str(a):
        b = b+(int(i)**2)
    a = b
if a == 1:
    print (f"{num} is a Happy number")
else:
    print(f"{num} is not a Happy number")