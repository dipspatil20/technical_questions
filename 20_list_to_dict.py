key = ["name", "age", "city"]
val=["Rome", 22, "Delhi"]
d ={}
for i in range (len(key)):
    d[key[i]]=val[i]
print(d)


v = dict(zip(key,val))
print(v)