import collections
import heapq
def check(qs):
    answer = -1e9
    for q in qs:
        answer = max(answer, q[0])
    return answer
def solution(priorities, location):
    answer = 0
    q = collections.deque()
    qs = collections.deque()
    for i, p in enumerate(priorities):
        q.append([p, i])
    while q:
        x = q.popleft()
        if check(q) <= x[0]:
            qs.append(x[1])
        else:
            q.append(x)

    for i, v in enumerate(qs):
        if v == location:
            return i+1
    return answer

solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1]	, 0)