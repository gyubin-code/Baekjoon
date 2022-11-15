import itertools
import sys

input = sys.stdin.readline


data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(itertools.permutations(data, 3))

n = int(input())

for _ in range(n):
    n, s, b = map(int, input().split())
    n = list(str(n))
    removeCount = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= removeCount
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1

        if (strike != s) or (ball != b):
            num.remove(num[i])
            removeCount += 1

print(len(num))

