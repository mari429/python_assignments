# 5.	Write a Python program to determine whether the given number is a Harshad Number?
num = 27
sum_num = 0
for i in str(num):
    sum_num = sum_num + int(i)
if num%sum_num == 0:
    print (f"{num} is a Harshad number")
else:
    print(f"{num} is not a Harshad number")