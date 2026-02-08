num = 153
temp = num
sum =0
n=len(str(num))
while temp>0:
    digit = temp%10
    sum = sum+(digit**n)
    temp = temp//10
if num==sum:
    print(True)
else:
    print(False)
