import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (1000001)
arr[1] = 1
arr[2] = 2

def dp(x):
    for i in range(3, 1000001):
        arr[i] = (arr[i-1] + arr[i-2])%15746
    return arr[x]

print(dp(n))