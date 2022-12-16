def solution(arr):
    answer = 0
    arr.sort()
    answer = arr[-1] * arr[-2] * arr[-3]
    # print(answer)
    return answer

solution([-3, 1, 2, -2, 5, 6])