num = int(input("enter num"))
# s="madam"


temp=num
rev=0

while temp>0:
    digit=temp%10
    rev = rev*10+digit
    temp = temp//10

if num==rev:
    print('palindrom')
else:
    print('not palindrome')