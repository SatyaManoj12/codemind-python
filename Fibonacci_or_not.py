n=int(input())
f1=0
f2=1
f3=1
if n==0 or n==1:
    printf("True")
else:
    while f3<n:
        f3=f1+f2
        f2=f1
        f1=f3
    if f3==n:
        print("True")
    else:
        print("False")