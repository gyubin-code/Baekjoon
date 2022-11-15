import sys, heapq
input = sys.stdin.readline
v, e = map(int, input().split())
s = int(input())

arr = [[] for _ in range(v+1)]

dp = [1e9]*(v+1)

heap = []

for i in range(e):
    start, end, weight = map(int, input().split())
    #바로 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용하는 것입니다.
    arr[start].append((weight, end))

def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))


    while heap:
        wei, now = heapq.heappop(heap)

        if dp[now] < wei:
            continue

        for w, next_node in arr[now]:
            next_wei = w + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))

dijkstra(s)
for i in range(1, v+1):
    print("INF" if dp[i] == 1e9 else dp[i])


