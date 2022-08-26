def matrix_add(a,b):
    d = []
    if len(a) == len (b):
        for i in range (len(a)):
            c = []
            if len(a[i]) == len(b[i]):
                for j in range (len(a[i])):
                    c.append(a[i][j]+b[i][j])
                d.append(c)
            else:
                print("Only similar arrays can be added")
                break
        else:
            return d
a = [[1,2,3],[3,4,6],[3,9,7]]
b = [[5,6,1],[7,8,0],[6,9,2]]
print(matrix_add(a,b))
