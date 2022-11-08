import sys, itertools

input = sys.stdin.readline

n, m = map(int, input().split())

s = []

def dfs(k):
    if len(s) == m:
        print(*s)

    for i in range(k+1, n+1):
        s.append(i)
        dfs(i)
        s.pop()

dfs(0)