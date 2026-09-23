num = 4
if num%2==0:
    print("Even")
else:
    print("Odd")

if num<=0:
    print("not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("not Prime")
            break
    else:
        print("prime")

fact=1
for j in range(1,num+1):
    fact *= j
print("fact", fact)

a,b=0,1
for i in range(num):
    