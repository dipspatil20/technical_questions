l1 = [1,2,4,3,7,8,5,9,6,7,3,5,5,9,6,7,2,6,4]
feq={}
for i in l1:
    if i in feq:
        feq[i]+=1
    else:
        feq[i]=1

print(feq)