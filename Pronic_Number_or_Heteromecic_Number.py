n=int(input())
x=0
for i in range(n):
    if(i*(i+1)==n):
        x=1
if(x==1):
    print("YES")
else:
    print("NO")