# 5.	Write a Python Program to check if given array is Monotonic?
# l = [3,4,5,6,7,8,9,27,29,45,84,96,102]
l = [102, 96, 84, 45, 29, 27, 9, 8, 7, 6, 5, 4, 3]
# l = [102, 84, 96, 9, 45, 29, 4, 27, 9, 8, 7, 6, 5, 3]
k,p,i,j=0,0,0,0
while i<len(l)-1:
    if l[i]<=l[i+1]:
        i+=1
        continue
    else:
        k+=1
        break
else:
    k-=1
while j<len(l)-1:
    if l[j]>=l[j+1]:
        j+=1
        continue
    else:
        p+=1
        break
else:
    p-=1
# print (k, "   ", p)
if k == -1 or p == -1:
    print("Thi array is monotonic")
else:
    print ("This array is not monotonic")




