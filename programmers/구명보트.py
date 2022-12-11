import collections


def solution(people, limit):
    answer = 0
    people.sort()

    q = collections.deque(people)

    while q:
        if len(q) > 1:
            if q[0] + q[-1] > limit:
                answer += 1
                q.pop()
            elif q[0] + q[-1] <= limit:
                q.popleft()
                q.pop()
                answer += 1
        else:
            answer += 1
            q.pop()

    return answer
#
solution([70,30,70,30], 100)
solution([70, 50, 80, 50], 100)
solution([100,100,100,100,100], 100)
solution([70, 80, 50], 100)