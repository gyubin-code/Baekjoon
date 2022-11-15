import sys
input = sys.stdin.readline
a, b = map(int, input().split())

black_board = [["W", "B", "W", "B", "W", "B", "W", "B"],["B", "W", "B", "W", "B", "W", "B", "W"]] * 4
white_board = [["B", "W", "B", "W", "B", "W", "B", "W"], ["W", "B", "W", "B", "W", "B", "W", "B"]] * 4


board = [list(input().rstrip()) for _ in range(a)]

def find(m, n):
    # 어떤 위치에서 보드를 2번 검사하여 ( 검은경우 흰 경우 ) 더 작은 수를 출력한다
    # 검은 경우
    black = 0
    for j in range(n, n+8):
        for i in range(m, m+8):
            if board[j][i] != black_board[j-n][i-m]:
                black += 1
    white = 0
    for j in range(n, n+8):
        for i in range(m, m+8):
            if board[j][i] != white_board[j-n][i-m]:
                white += 1

    return min(black, white)

answer = 1e9
for j in range(a - 7):
    for i in range(b - 7):
        answer = min(find(i, j), answer)

print(answer)
