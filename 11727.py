testcase=int(input())
# append를 사용해서 풀어보았다
dp = [0, 1, 3]

for i in range(3,1001):
    dp.append((dp[i - 2] * 2) + dp[i - 1])

print(dp[testcase]%10007)