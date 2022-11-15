import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(input().rstrip()))
dx = 1
dy = 1

# 처음 보드에서 가장 긴 수열길이 찾기
def search_row(board):
    answer = 1
    # c c c 이런식으로 찾기
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+dx]:
                cnt += 1
                answer = max(cnt, answer)
            else:
                cnt = 1
    return answer

def search_col(board):
    answer = 1
    # c
    # c
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[j][i] == board[j+dy][i]:
                cnt += 1
                answer = max(cnt, answer)
            else:
                cnt = 1
    return answer



def solve():
    answer_c = 1
    answer_r = 1
    answer = 1
    for i in range(n):
        for j in range(n):
            if j != n-1:
                # 바꾸기
                tmp = arr[i][j]
                arr[i][j] = arr[i][j+dx]
                arr[i][j + dx] = tmp

                cnt1 = search_col(arr)
                cnt2 = search_row(arr)
                answer = max(cnt1 , cnt2, answer)

                # 되돌리기
                tmp = arr[i][j]
                arr[i][j] = arr[i][j + dx]
                arr[i][j + dx] = tmp

            if i != n-1:
                tmp = arr[i][j]
                arr[i][j] = arr[i+dy][j]
                arr[i+dy][j] = tmp

                cnt1 = search_col(arr)
                cnt2 = search_row(arr)
                answer = max(cnt1, cnt2, answer)

                tmp = arr[i][j]
                arr[i][j] = arr[i+dy][j]
                arr[i+dy][j] = tmp


    print(answer)

solve()
