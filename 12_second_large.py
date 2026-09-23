l = [10,20,30,40,15,35]
first = second = float("-inf")
for i in l:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=i
print(second)