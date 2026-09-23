l1 = [1,2,4,3,7,8,5,9,6,7] 
l2 = [3,5,5,9,6,7,2,6,4]

result=[]
for i in l1:
    if i in l2:
        result.append(i)
print(result)