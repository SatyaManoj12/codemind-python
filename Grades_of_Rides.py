k,l,m=map(int,input().split())
if(k>50 and l>60 and m>100):
    print('10')
elif(k>50 and l>60):
    print('9')
elif(l>60 and m>100):
    print('8')
elif(k>50 and m>100):
    print('7')
elif(k>50 or l>60 or m>100):
    print('6')
else:
    print('5')
