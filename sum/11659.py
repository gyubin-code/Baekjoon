import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = list(map(int, input().split()))
s = [0, arr[0]]

for i, v in enumerate(arr):
    if i == 0:
        continue
    s.append(s[i] + v)



for _ in range(m):
    i, j = map(int, input().split())

    print(s[j]-s[i-1])

