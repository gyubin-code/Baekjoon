n= int(input())


max = 100000
dp = [[0]*3 for _ in range(max+1)]

dp[1]=[1,0,0]
dp[2]=[0,1,0]
dp[3]=[1,1,1]
m =1000000009
# i) dp[n][1] = dp[n-1][2] + dp[n-1][3]

#  ii) dp[n][2] = dp[n-2][1] + dp[n-2][3]

#  iii) dp[n][3] = dp[n-3][1] + dp[n-3][2]
# 위 점화식이 키 포인트이다.

for i in range(4,max+1):
    dp[i][0]=(dp[i-1][1]+dp[i-1][2])
    dp[i][1]=dp[i-2][0]+dp[i-2][2]
    dp[i][2]=(dp[i-3][0]+dp[i-3][1])
    dp[i][0]%=m
    dp[i][1]%=m
    dp[i][2]%=m
   # dp.append(list([(dp[i-1][1]+dp[i-1][2]),(dp[i-2][0]+dp[i-2][2])%m,(dp[i-3][0]+dp[i-3][1])%m]))

for i in range(n):
    a = int(input())
    
    print(sum(dp[a])%m)