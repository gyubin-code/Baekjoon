import heapq
def solution(scoville, K):
    answer = 0
    q = []
    for s in range(len(scoville)):
        heapq.heappush(q, scoville[s])

    if scoville[-1] == 0 and scoville[-2] == 0:
        return -1

    while q:
        if q[0] >= K:
            break
        if len(q) == 1 and min(q) < K:
            answer = -1
            break
        f = heapq.heappop(q)
        s = heapq.heappop(q)
        x = f + s * 2
        heapq.heappush(q, x)
        answer += 1

    return answer

solution([1, 2, 3, 9, 10, 12], 7)
solution([0, 1], 8)