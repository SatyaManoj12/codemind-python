n=int(input())
sum=0
for i in range(2,n):
    if n%i==0:
        sum+=i
if sum>n:
    print('True')
else:
    print('False')