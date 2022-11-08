import sys

lambda input: sys.stdin.readline().rstrip

if __name__ == '__main__':
    n = int(input())
    arrs = [[] for i in range(501)]
    for i in range(1, n+1):
        arrs[i] += list(map(int, input().split()))

    dp = [0] * (n+1)
    visit = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        time = 0
        for j in range(len(arrs[i])-1):
            # 만약 이전에 방문하지 않았을 경우에
            # 우선 지어야하는 애들의 값을 가져오고
            # 이후 우선 지은애들은 뭘 지었는지 가져온다
            if j == 0:
                time = arrs[i][0]
            else:
                if arrs[i][j] not in visit[i]:
                    dp[i] += dp[arrs[i][j]]
                    visit[i] += visit[arrs[i][j]]

        dp[i] += arrs[i][0]
        visit[i].append(i)
        #print(visit)
        print(dp[i])







