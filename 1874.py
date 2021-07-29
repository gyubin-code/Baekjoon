import sys 
input = sys.stdin.readline

n = int(input())


dp=[0]*301
arr=[0]


for i in range(1,n+1):
    arr.append(int(input()))
dp[0]=0
dp[1]=arr[1]
dp[2]=max(arr[1]+arr[2],arr[2])
dp[3]=max(arr[1]+arr[3],arr[1]+arr[2])

for i in range(3,n+1):
    dp[i]= max(dp[i-3]+arr[i]+arr[i-1],dp[i-2]+arr[i])

print(dp[n])