n=int(input())
sum=0
m=n*n
while(m>0):
    r=m%10
    sum=sum+r
    m=m//10
if(n==sum):
    print("Neon Number")
else:
    print("Not Neon Number")