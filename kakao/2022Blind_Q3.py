

def set_board(board , f, a, b, c, d, m):
    if f == 1:
        m = - m
    for i in range(b, d+1):
        for j in range(a, c+1):
            board[j][i] += m


    return board

# def solution(board, skill):
#     answer = 0
#     for s in skill:
#         f = s[0]
#         a = s[1]
#         b = s[2]
#         c = s[3]
#         d = s[4]
#         m = s[5]
#         board = set_board(board, f, a, b, c, d, m)
#
#     for j in range(len(board)):
#         for i in range(len(board[0])):
#             if board[j][i] > 0:
#                 answer += 1
#
#     print(answer)
#     return answer

def solution(board, skill):
    answer = 0
    # 누적합 풀이
    new_board = [[0]* len(board[0]) for _ in range(len(board))]

    for s in skill:
        new_board


    print(answer)
    return answer
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

solution(board, skill)

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

solution(board, skill)