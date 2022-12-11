def solution(progresses, speeds):
    answer = []
    q = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            q.append((100-progresses[i])//speeds[i])
        else:
            q.append((100-progresses[i])//speeds[i] + 1)
    # print(q)
    tmp = 0
    t = q[0]
    for i in q:
        if i > t:
            t = i
            answer.append(tmp)
            tmp = 1
        else:
            tmp += 1
    answer.append(tmp)
    # print(answer)

    return answer
solution([93, 30, 55], 	[1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])