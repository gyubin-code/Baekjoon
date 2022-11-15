import sys

input = sys.stdin.readline

n = int(input())
arr = []
visit = [0] * (n+1)

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[0])

board = [[] for _ in range(n+1)]

# print(arr)

for i in range(1, n+1):
    for j in range(n):
        if arr[j][0] >= i:
            board[i].append([arr[j][0],arr[j][1],j])

answer = 0
for i in range(n, 0, -1):
    board[i].sort(key=lambda x: -x[1])
    # print(board[i])
    flag = 0
    for b in board[i]:
        if visit[b[2]] == 0 and flag == 0:
            visit[b[2]] = 1
            flag = 1
            answer += b[1]
            # print(b[1])

print(answer)
