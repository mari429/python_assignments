# 5.	Write a Python program to find uncommon words from two Strings?
txt1 = "He works in xyz organization"
txt2 = "The organization he works excels in its field"
for i in (txt1+" "+txt2).split():
    if (txt1+" "+txt2).count(i) == 1:
        print(i)
