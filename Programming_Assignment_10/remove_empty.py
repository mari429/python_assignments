# 9.	Write a Python program to Remove empty List from List?
l = ["Ramesh","Suresh",[],"Akhil","Ganesh",[],"Manu","Vishal","Rohith"]
for i in l:
    if i == []:
        l.remove(i)
print(l)
