b = [[5,6,1],[7,8,0],[6,9,2]]
d = []
for i in range(len(b)):
    c= []
    for j in range(len(b[i])):
        c.append(b[j][i])
    d.append(c)
print(d)