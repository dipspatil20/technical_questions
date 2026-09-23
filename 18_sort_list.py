l1 = [1,2,4,3,7,8,5,9,6,7,3,5,5,9,6,7,2,6,4]

for i in range(len(l1)):
    for j in range(len(l1)-1):
        if l1[j] > l1[j+1]:
            l1[j], l1[j+1] = l1[j+1], l1[j]
print(l1)