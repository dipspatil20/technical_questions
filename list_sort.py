num = [2,4,6,2,5,3,8]
new = []
while len(num)>0:
    small = num[0]
    for n in num:
        if n < small:
            small = n

    new.append(small)
    num.remove(small)
print(new)
