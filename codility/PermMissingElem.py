def solution(A):
    if len(A) == 0:
        result = 1
    else :
        result = sum(range(1, len(A)+2)) - sum(A)
    return result

solution([1,2,3,5])
solution([])
print(solution([2]))
solution([1,2,4])
solution([2,3,4,5])
