def solution(number, k):
    answer = ''
    need_cnt = len(number) - k
    front = 0

    while 1:
        tmp, x = "", 0
        for i, v in enumerate(number[front: len(number) - need_cnt+1]):
            if v == '9':
                tmp = v
                x = front + i
                break
            elif v > tmp:
                tmp = v
                x = front+i

        front = x+1
        need_cnt -= 1
        answer += tmp

        if need_cnt == 0:
            break



    # print(answer)

    return answer

# solution("1924", 2)
# solution("1231234", 3)
# solution("4177252841", 4)
# solution('321', 1)
solution('999', 1)