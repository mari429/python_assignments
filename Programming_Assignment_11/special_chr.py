# 7.	Write a Python Program to check if a string contains any special character?
txt1 = '''ineuron'''
for i in txt1:
    if ord(i.upper())>=65 and ord(i.upper())<=90:
        continue
    else:
        print("This string has special character")
        break
else:
    print("This string don't have any special character")