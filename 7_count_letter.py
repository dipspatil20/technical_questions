s = "hello"
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

vowel =0
consonent=0
check="aeiou"
for i in s:
    check.upper()
    if i in check:
        vowel+=1
    else:
        consonent+=1
print("consonent ",consonent)
print("vowel ", vowel)