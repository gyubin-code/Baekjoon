import collections


def solution(n, s, a, b, fares):
    answer = 1e9
    board = [[1e9] * (n +1) for _ in range(n+1)]

    for i in range(1, n+1):
        board[i][i] = 0

    for f in fares:
        board[f[0]][f[1]] = f[2]
        board[f[1]][f[0]] = f[2]

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if board[i][k] == 1e9 or board[k][i] == 1e9:
                    continue
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])


    for i in range(1, n+1):
        answer = min(answer, board[s][i] + board[i][b] + board[i][a])

    print(answer)
    return answer


solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])