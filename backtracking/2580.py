import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    arr.append(list(map(int, input().split(' '))))

basic = range(1, 10)

zeros = []
for j in range(9):
    for i in range(9):
        if arr[j][i] == 0:
            zeros.append((i, j))


def promissing(i, j):
    global arr
    # 가로 검사
    if arr[j].count(arr[j][i]) == 2:
        return False
    # 세로 검사
    tmp = []
    for t in range(9):
        if arr[t][i] != 0 and arr[t][i] in tmp:
            return False
        tmp.append(arr[t][i])
    # 섹션 검사
    # 0~2/ 3~5/6~8
    tmp = []
    col = (i // 3) * 3 # 가로
    row = (j // 3) * 3# 세로
    for i in range(col, col + 3):
        for j in range(row, row + 3):
            if arr[j][i] != 0:
                if arr[j][i] in tmp:
                    return False
                tmp.append(arr[j][i])

    return True

def nqueen(n):
    global arr

    if n == len(zeros):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end=' ')
            print()
        exit(0)

    else:
        (i, j) = zeros[n]
        for num in basic:
            arr[j][i] = num
            if promissing(i, j):
                nqueen(n+1)
            arr[j][i] = 0


nqueen(0)

