import sys, collections

input = sys.stdin.readline
n = int(input())
board = [[0] * 2 for _ in range(n)]
a, b = 0, 0

for i in range(n):
    a, b = map(int, input().split())
    board[i][0], board[i][1] = a, b

# 가능한 회의 중에서 가장 먼저 끝나는 회의 선택
# 적절하게 정렬한 후에 가장 먼저 끝나는 회의를 선택
board.sort(key=lambda x: (x[1], x[0]))

cur = 0
cnt = 0
for i in range(n):
    if cur <= board[i][0]:
        cur = board[i][1]
        cnt += 1

print(cnt)
