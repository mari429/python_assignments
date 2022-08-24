# 5.	Write a Python Program to check if given array is Monotonic?

l = [102, 96, 84, 45, 29, 27, 9, 8, 7, 6, 5, 4, 3]
# l = [3,4,5,6,7,8,9,27,29,45,84,96,102]
# l = [102, 84, 96, 9, 45, 29, 4, 27, 9, 8, 7, 6, 5, 3]
if all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1)):
    print ("monotoni array")
else:
    print ("Not a monotonic array")

# l = [102, 96, 84, 45, 29, 27, 9, 8, 7, 6, 5, 4, 3]
# l = [3,4,5,6,7,8,9,27,29,45,84,96,102]
# l = [102, 84, 96, 9, 45, 29, 4, 27, 9, 8, 7, 6, 5, 3]
# print(monotonic_array(l))