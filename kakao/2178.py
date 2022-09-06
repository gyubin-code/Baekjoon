import collections
import sys

n, m = map(int, input().split())
board = list()
dist = [[-1] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

q = collections.deque()

# 입력 받기
board = [sys.stdin.readline().rstrip() for _ in range(n)]

q.append([0, 0]) # x, y
dist[0][0] = 1 # 처음 거리는 1

while q:
    xy = q.popleft()

    for i in range(4):
        x = xy[0] + dx[i]
        y = xy[1] + dy[i]
        # 방문, 범위, 조건
        if 0 <= x < m and 0 <= y < n and board[y][x] == '1' and dist[y][x] == -1:
            q.append([x, y])
            dist[y][x] = dist[xy[1]][xy[0]] + 1


print(dist[n-1][m-1])


