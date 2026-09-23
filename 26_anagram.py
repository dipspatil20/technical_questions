s1 = "listens"
s2="silent"
#method 1
if sorted(s1)==sorted(s2):
    print(True)
else:
    print(False)

#method 2
if len(s1)!=len(s2):
    print(False)
else:
    f1={}
    f2={}
    for i in s1:
        if i in f1:
            f1[i]+=1
        else:
            f1[i]=1
    for i in s2:
        if i in f2:
            f2[i]+=1
        else:
            f2[i]=1
    if f1==f2:
        print(True)
    else:
        print(False)