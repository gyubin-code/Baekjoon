
n = int(input())

arr=[[0]*n for _ in range(2)]

arr[0]=list(map(int,input().split()))
arr[1]=list(map(int,input().split()))

cnt =100
point =0
for i in range(n):
    cnt-=arr[0][i]
    if(cnt>0):
        point+=arr[1][i]        
    elif(cnt<=0):
        print(point)




