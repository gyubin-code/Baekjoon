import sys
input = sys.stdin.readline

num = 100001
res = [-1e9] * num

n = int(input())
arr = list(map(int, input().split()))


res[0] = arr[0]
for i in range(1, n):
    res[i] = max(res[i-1] + arr[i], arr[i], res[i] )


print(max(res))