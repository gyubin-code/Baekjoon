n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])
        

#만약 내 날짜에서 0열의 값을 더했을때 days 보다 같거나 크다면 , 최소비용을 갱신할수 없음
    # 만약 3일에 일을 하게 되서 4일째 일을 못하게된다면 dp에 기록된 최소비용을 비교하여 선택함


