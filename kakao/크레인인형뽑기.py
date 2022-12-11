import collections
def solution(board, moves):
    answer = 0
    leny = len(board)
    lenx = len(board[0])
    q = collections.deque()
    depth = [0] * 31 # 최초의 깊이
    for i in range(lenx):
        for j in range(leny):
            if board[j][i] != 0:
                depth[i] = j
                break

    for X in moves:
        x = X-1 # 위치
        dy = depth[x]
        if q:
            if q[-1] == board[dy][x]:
                q.pop()
                answer += 2
            else:
                q.append(board[dy][x])
        else:
            q.append(board[dy][x])

        if depth[x] != len(board)-1:
            depth[x] += 1


    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))
