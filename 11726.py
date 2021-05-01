testcase=input()
testcase=int(testcase)
# 123더하기에서 참고해서 풀었다 9095번
dp=[0]*(1001)

dp[1]=1
dp[2]=2

for i in range(3,1001):
    dp[i]=dp[i-2]+dp[i-1]

print(dp[testcase]%10007)

