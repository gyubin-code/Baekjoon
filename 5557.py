import sys

lambda input: sys.stdin.readline().rstrip


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(" ")))


    dp = list()
    dp = [[0] * 21 for _ in range(n)]

    dp[0][arr[0]] = 1

    for i in range(1, n-1):
        for j in range(21):
            if dp[i-1][j]:
                if -1 < j + arr[i] < 21:
                    dp[i][j + arr[i]] += dp[i-1][j]
                if -1 < j - arr[i] < 21:
                    dp[i][j - arr[i]] += dp[i-1][j]

    print(dp[n-2][arr[-1]])

