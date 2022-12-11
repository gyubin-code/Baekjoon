def solution(arr):
    answer = [arr[0]]
    for a in arr:
        if answer[-1] != a:
            answer.append(a)
    return answer

print(solution([1,1,3,3,0,1,1]))