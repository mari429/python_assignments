# 4.	Write a Python to check if a given string is binary string or not?
txt = "1010101110"
for i in txt:
    if int(i)==0 or int(i)==1:
        continue
    else:
        print("Non-Binary string")
        break
else:
    print("Binary string")