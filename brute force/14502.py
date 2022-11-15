import itertools
import sys, collections, copy

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] # 원본
board = copy.deepcopy(arr)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rq = collections.deque()
nums = []

for j in range(n):
    for i in range(m):
        if board[j][i] == 2:
            rq.append((i, j))
        elif board[j][i] == 0:
            nums.append(j*m+i)


def solve(comb , board, q):
    cnt = 0

    for c in comb:
        board[c//m][c%m] = 1

    def bfs(q):
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if board[ny][nx] == 0 and board[ny][nx] != 1:
                        board[ny][nx] = 2
                        q.append((nx, ny))

    bfs(q)
    for j in range(n):
        for i in range(m):
            if board[j][i] == 0:
                cnt += 1

    return cnt


answer = -1e9
for comb in itertools.combinations(nums, 3):
    board = copy.deepcopy(arr)
    q = copy.deepcopy(rq)
    cnt = solve(comb, board, q)
    answer = max(answer, cnt)


print(answer)