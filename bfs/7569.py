import sys
input = sys.stdin.readline


m, n, h = map(int, input().split())

arr = []
second = [] # 2차원 배열

# 3차원 배열 결정
for i in range(n*h):
    second.append(list(map(int, input().split())))
    if i % n == n-1:
        arr.append(second)
        second = []

# 초기 설정
q = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                # x / y / x
                q.append((k, j, i))

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, 0, -1]
dz = [1, -1]

visited = [[[-1] * m for _ in range(n)] for _ in range(h)]





