def solution(arr):
    # write your code in Python 3.8.10

    n = len(arr)
    cnt = arr[0] - sum(arr[1:])
    if n == 2:
        return abs(cnt)
    answer = abs(cnt)
    for p in range(2, n):
        cnt += 2*arr[p-1]
        answer = min(abs(cnt), answer)
    return answer


print(solution([1,2,3]))
# print(solution([-100,100]))
# print(solution([100,100]))
# print(solution([0,-15]))
print(solution([3,1,2,4,3]))
