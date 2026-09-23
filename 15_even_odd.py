l1 = [1,2,4,3,7,8,5,9,6,7,3,5,5,9,6,7,2,6,4,9]
even=0
odd=0
for i in l1:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even",even)
print("odd",odd)