n=int(input())
a,b=0,1
i=2
print(a,b,end=' ')
while i<n:
     c=a+b
     print(c,end=' ')
     a=b
     b=c
     i+=1