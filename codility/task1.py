def solution(N):
    # write your code in Python 3.8.10
    binaryNum = format(N, 'b')
    answer = 0
    flag = 0
    cnt = 0
    for b in str(binaryNum):
        if b == "1":
            if flag == 1:
                answer = max(answer, cnt)
                cnt = 0
            flag = 1
        else:
            if flag == 1:
                cnt += 1
    print(answer)
    return answer

solution(20)