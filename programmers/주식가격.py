def solution(prices):
    answer =[0] * len(prices)
    for i in range(len(prices)):
        tmp = 0
        for j in range(i+1, len(prices)):
            tmp += 1
            if prices[j] < prices[i]:
                break
        answer[i] = tmp
    return answer

solution([1, 2, 3, 2, 3])