n = int(input())

if(n==1):
    print(-1)
elif(n==3):
    print(-1)
else:
    
    coin5=int(n/5)
    n= n-5*coin5
    if n%2==1:
        coin5-=1
        n+=5
    coin2=n/2
    print(int(coin2+coin5))

