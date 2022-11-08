def solution(n, m, x, y, r, c, k):
    answer = []
    board = [[0]* (m) for _ in range(n)]
    visited = [[0]* (m) for _ in range(n)]
    board[x-1][y-1] = 1 # 출발지
    board[r-1][c-1] = 1

    dx = [1, 0, -1, 0] # r, l, d, u
    dy = [0, 1, 0, -1] # 0, 1, 2, 3

    dic = {0: 'r', 1: 'u', 2: 'l', 3: 'd'}


    def dfs(a, b, t): # x, y
        if a == c-1 and b == r-1:
            answer.append(t)
            return

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            # 범위, 방문, 조건
            if 0<= nx< m and 0 <= ny < n :
                visited[ny][nx] = visited[b][a] + 1
                dfs(nx, ny, dic[i] + t)
                visited[ny][nx] = visited[b][a] - 1

    dfs(y-1, x-1, '')

    print(answer)

    return answer
solution(3, 4, 2, 3, 3, 1, 5)