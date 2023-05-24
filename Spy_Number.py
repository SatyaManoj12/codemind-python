n=int(input())
sum=0
mul=1
while(n>0):
    r=n%10
    sum=sum+r
    mul=mul*r
    n=n//10
if(mul==sum):
    print("Spy Number")
else:
    print("Not Spy Number")