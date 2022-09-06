import collections
import sys

n, m = map(int, input().split())
board = list()
visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

q = collections.deque()

# 입력 받기
for _ in range(n):
    input_line = sys.stdin.readline().rstrip().split()
    board.append(input_line)

# bfs 함수화
def bfs(i:int , j: int):
    visited[i][j] = True
    q.append([i, j])

    width = 1

    while q:
        yx = q.pop()
        for i in range(4):
            x = yx[1] + dx[i]
            y = yx[0] + dy[i]
            # 범위, 방문 여부 , 조건
            if 0 <= x < m and 0 <= y < n and visited[y][x] == False and board[y][x] == '1':
                visited[y][x] = True
                q.append([y, x])
                width += 1
    return visited, width


max_width = 0
cnt_paint = 0

for i in range(n):
    # -> 방향으로 체크
    for j in range(m):
        if board[i][j] == '1' and visited[i][j] == False:
            visited, width = bfs(i, j)
            max_width = max(max_width, width)
            cnt_paint += 1

print(cnt_paint)
print(max_width)
