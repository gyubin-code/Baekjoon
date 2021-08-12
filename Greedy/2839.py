n =int(input())
a=0
b=0
ans =5000/3
i=0
max_Cnt = int(n/3)
while(max_Cnt+1!=i):
    
    tmp_n = n-3*b
    
    if(tmp_n == 0):
        ans= min(ans,b)
    if(tmp_n%5==0): #나누어 떨어지는 경우
        a=tmp_n/5
        ans = min(ans,a+b)
    b+=1
    i+=1
if(ans == 5000/3):
    print(-1)
else:print(int(ans))