# 1.	Write a Python program to check if the given number is a Disarium Number?
a = 175
b = 0
for i in str(a):
    b = b + (int(i)**(int(str(a).index(i))+1))
if b == a:
    print(f"The number {a} is Disarium number")
