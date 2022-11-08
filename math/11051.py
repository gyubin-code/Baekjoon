import sys

lambda input: sys.stdin.readline().rstrip

def solve(n, k):
    dp[1][1] = 1
    for i in range(2, 1002):
        for j in range(1, i+1):
            if j == 1:
                dp[i][j] = 1
            elif j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


    print(dp[n+1][k+1] % 10007)



if __name__ == '__main__':
    n, k = map(int, input().split())

    dp = list()
    dp = [[0] * 1002 for _ in range(1003)]

    # dp[n][k]

    solve(n, k)



