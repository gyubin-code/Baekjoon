# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.8.10

    n = len(A)
    if n == 0:
        return A
    start = -K % n
    cnt = 0
    arr = []

    while 1:
        if cnt == n:
            break
        arr.append(A[start])
        start = (start + 1) % n
        cnt += 1
    # print(arr)
    return arr

# solution([3, 8, 9, 7, 6], 8)
# solution([1, 2, 3, 4], 4)
# solution([0,0,0], 3)
solution([], 1)