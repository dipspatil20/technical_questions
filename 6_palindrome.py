s="level"
rev = ""
for i in s:
    rev = i+rev
if s==rev:
    print(True)
else:
    print(False)

a=12321
check =0
temp = a
while temp>0:
    digit = temp %10
    check =check*10+digit
    temp= temp//10
if check==a:
    print(True)
else:
    print(False)
