import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

answer = 0
for c in coins:
    if k < 0:
        break
    if c > k:
        continue

    answer += k // c
    k = k % c


print(answer)