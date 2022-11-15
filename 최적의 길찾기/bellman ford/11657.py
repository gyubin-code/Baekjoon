import sys, heapq
input = sys.stdin.readline
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]

dp = [1e9] * (v+1)
heap = []

for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))


def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        wei, now = heapq.heappop(heap)

        if dp[now] < wei:
            continue

        for w, nn in graph[now]:
            nw = w + wei
            if nw < dp[nn]:
                dp[nn] = nw
                heapq.heappush(heap, (nw, nn))

dijkstra(1)
print(dp)
