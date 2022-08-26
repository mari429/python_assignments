a = [[1,1,1],[1,1,1],[1,1,1]]
b = [[1,1,1],[1,1,1],[1,1,1]]
f = []
for i in range(len(a)):
    d = []
    for j in range(len(b[0])):
        c=0
        for p in range(len(b)):
            c= c + ( a[i][p] * b[p][j] )
        d.append(c)
    f.append(d)
print(f)