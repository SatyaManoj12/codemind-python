n=int(input())
temp=n
rem=0
while n>0:
    r=n%10
    rem=rem*10+r
    n=n//10
if(rem==temp):
    print('True')
else:
    print('False')