import collections


def solution(queue1, queue2):
    q1, total1 = collections.deque(), 0
    q2, total2 = collections.deque(), 0
    n = len(queue1 + queue2)
    answer = -1
    for i in queue1:
        q1.append(i)
        total1 += i

    for i in queue2:
        q2.append(i)
        total2 += i

    for i in range(600001):
        if total1 == total2:
            return i

        if total1 < total2:
            z = q2.popleft()
            total1 += z
            total2 -= z
            q1.append(z)
        else:
            z = q1.popleft()
            total2 += z
            total1 -= z
            q2.append(z)
    return -1

