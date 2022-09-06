import sys
import collections

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())

# 보드 받음
board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

fire_q = collections.deque()
# 불이 이동하는 시간 -> -1이면 불의 영향을 안받는곳
fire_dist = [[-1] * c for _ in range(r)]

j_q = collections.deque()
# 사람이 이동하는곳
j_dist = [[-1] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        # 불난곳 위치
        if board[i][j] == 'F':
            fire_q.append((j, i))
            fire_dist[i][j] = 0
        # 사람 위치
        elif board[i][j] == 'J':
            j_q.append((j, i))
            j_dist[i][j] = 0


def bfs():

    # 갹 위치에 불이 붙는 시간 = fire_dist
    while fire_q:
        x, y = fire_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위, 방문, 조건
            if 0 <= nx < c and 0 <= ny < r:
                if fire_dist[ny][nx] == -1 and board[ny][nx] != '#':
                    fire_dist[ny][nx] = fire_dist[y][x] + 1
                    fire_q.append((nx, ny))
    # 불 붙는위치 확인
    # for i in range(r):
    #     print(fire_dist[i])

    # j는 불이 붙는 시간보다 빨리 도착하면 갈수있는 길이다.
    answer = 0
    while j_q:
        x, y = j_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= c or ny < 0 or ny >= r:
                answer = j_dist[y][x] + 1
                # 큐가 남을수도 있다.
                return answer

            # 범위, 방문, 조건
            elif 0 <= nx < c and 0 <= ny < r: # 범위
                if board[ny][nx] != '#' and j_dist[ny][nx] == -1:
                    if fire_dist[ny][nx] == -1 or fire_dist[ny][nx] > j_dist[y][x] + 1: # 불의 영향을 받지 않거나 불 나기 전에 도착하거나
                        j_dist[ny][nx] = j_dist[y][x] + 1
                        j_q.append((nx, ny))

    return answer

answer = 0
answer = bfs()

if answer == 0:
    print('IMPOSSIBLE')
else:
    print(answer)

