import sys, copy, collections
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
H = 101
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def make_board(h, board):

    for j in range(n):
        for i in range(n):
            if board[j][i] <= h:
                board[j][i] = 1
            else:
                board[j][i] = 0

    return board

def solve(board):
    cnt = 0
    q = collections.deque()

    def bfs(q):
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[ny][nx] == 0:
                        q.append((nx, ny))
                        board[ny][nx] = 1




    for j in range(n):
        for i in range(n):
            if board[j][i] == 0:
                q.append((i, j))
                board[j][i] = 1
                bfs(q)
                cnt += 1


    return cnt


answer = -1e9
for h in range(1, 101):
    board = copy.deepcopy(arr)
    board = make_board(h, board)
    answer = max(answer, solve(board))

if answer == 0:
    answer = 1
print(answer)
