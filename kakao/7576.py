import sys
import collections
m, n = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

board = list()
visited = [[-1]*m for _ in range(n)]

board = [sys.stdin.readline().split() for _ in range(n)]

q = collections.deque()

minor_cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '1':
            q.append((j, i)) # x, y
            visited[i][j] = 0
        if board[i][j] == '-1':
            minor_cnt += 1


while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        # 범위, 방문, 조건
        if 0 <= nx < m and 0 <= ny < n:
            if visited[ny][nx] == -1 and board[ny][nx] != '-1':
                visited[ny][nx] = visited[y][x] + 1
                q.append((nx, ny))

# 모두 체크했는지 검사
def solve():
    max_date = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == -1:
                cnt += 1
            max_date = max(max_date, visited[i][j])

    if minor_cnt - cnt == 0:
        print(max_date)
    else:
        print(-1)
    return

solve()

