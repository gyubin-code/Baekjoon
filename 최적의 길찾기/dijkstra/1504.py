import sys, heapq
input = sys.stdin.readline
n, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
answer = 0
heap = []
arr = []

for i in range(v):
    start, end, w = map(int, input().split())
    graph[start].append((w, end))
    graph[end].append((w, start))
    arr.append((min(start,end), max(start, end), w))

px, py = sorted(map(int, input().split()))
k = 1e9

for i in range(v):
    if arr[i][0] == px and arr[i][1] == py:
        k = min(k, arr[i][2])

def dijkstra(start):
    dp = [1e9]*(n+1)
    heapq.heappush(heap, (0, start))
    dp[start] = 0
    while heap:
        wei, now = heapq.heappop(heap)
        if dp[now] < wei:
            continue
        for w, nn in graph[now]:
            nw = w + wei
            if nw < dp[nn]:
                dp[nn] = nw
                heapq.heappush(heap, (nw, nn))

    return dp

one = dijkstra(1)
v1 = dijkstra(px)
v2 = dijkstra(py)
cnt = 0
cnt = min(one[px] + v1[py] + v2[n], one[py] + v2[px] + v1[n])
print(cnt if cnt < 1e9 else -1)

