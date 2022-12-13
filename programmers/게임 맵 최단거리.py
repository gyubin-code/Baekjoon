import collections


def solution(maps):
    answer = 0
    visit = [[0] * len(maps[0]) for _ in range(len(maps))]
    len_x = len(maps[0])
    len_y = len(maps)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = collections.deque()
    q.append([0,0])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i] , y + dy[i]
            if 0 <= nx < len_x and 0 <= ny < len_y:
                if maps[ny][nx] == 1 and visit[ny][nx] == 0:
                    visit[ny][nx] = visit[y][x] + 1
                    q.append([nx, ny])

    if visit[len_y-1][len_x-1] == 0:
        answer = -1
    else:
        answer = visit[len_y-1][len_x-1]+1
    # print(answer)
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])