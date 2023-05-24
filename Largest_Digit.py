n=int(input())
l=0
while(n>0):
    rem=n%10
    if(l<rem):
        l=rem
    n=n/10
print(int(l))