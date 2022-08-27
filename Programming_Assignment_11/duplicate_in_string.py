# 6.	Write a Python to find all duplicate characters in string?
txt = "Mari Sankar"
duplicate = []
for i in txt:
    if txt.count(i) > 1 and i not in duplicate:
        duplicate.append(i)
print (duplicate)


