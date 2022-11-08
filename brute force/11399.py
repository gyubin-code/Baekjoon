import sys
n = int(input())
dp= list(map(int, sys.stdin.readline().split()))

dp.sort()
sum =0
for i in range(n):
    sum += dp[i]*(n-i)
print(sum)