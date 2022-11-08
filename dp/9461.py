import sys
input = sys.stdin.readline
arr = [0] * 101
arr[1] = 1
arr[2] = 1
arr[3] = 1
def dp(n):
    for i in range(4, 101):
        arr[i] = arr[i-2] + arr[i-3]

    return arr[n]

n = int(input())
for _ in range(n):
    print(dp(int(input())))