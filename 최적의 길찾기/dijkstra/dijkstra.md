# 다익스트라 최단 경로 

Dijkstra 알고리즘은 BFS와 굉장히 유사하며, 노드 사이 간선(Edge)에 양의 가중치를 갖는 그래프(음의 가중치 허용 X)에서 최단 경로를 찾을 때 사용할 수 있습니다.

heapq를 이용하여 가장 작은 가중치부터 순회한다.

## 특징
1. 간선간의 가중치
2. heapq 이용
3. start node 와 End 노드 간의 거리를 판별 가능 -> dp 이용
4. 방향성 여부 ( 양방향 vs 단방향 )

## 대표 코드
~~~python
import heapq
n = 100 # 노드 갯수
dp = [1e9] * (n + 1)
heap = []
graph = []
def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        wei, now = heapq.heappop(heap)
        if dp[now] < wei:
            continue
        for w, next_node in graph[now]:
            next_wei = w + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))
~~~~

## 대표문제
[최단경로 - 1753번](https://www.acmicpc.net/problem/1753)

[특정한 최단 경로 - 1504번](https://www.acmicpc.net/problem/1504)
