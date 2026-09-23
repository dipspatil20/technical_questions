l1 = [1,2,4,3,7,8,5,9,6,7] 
l2 = [3,5,5,9,6,7,2,6,4]
res = l1+l2
r=list(set(res))
print(r)


check=[]
for i in res:
    if i not in check:
        check.append(i)
print(check)
