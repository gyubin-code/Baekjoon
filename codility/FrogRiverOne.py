def solution(x, arr):
    # write your code in Python 3.8.10
    n = len(arr)
    visited = [0] * (x + 1)
    if n < x:
        return -1
    if n == 1 and x != 1:
        return -1
    new = [[] for _ in range(x+1)] # 위치가 접근하는 시간
    for i, v in enumerate(arr):
        new[v].append(i)

    answer = 0
    for i in range(1, len(new)):
        if len(new[i]) != 0:
            answer = max(answer, new[i][0])
        else:
            return -1
    # print(answer)
    return answer


solution(5, [1, 3, 1, 4, 2, 3, 5, 4])