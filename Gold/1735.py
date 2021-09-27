import sys
import heapq
inf = sys.maxsize
n,m = map(int,input().split())
start_node = int(input())
dp=[inf]*(n+1)
heap=[]
nodes = [[] for _ in range(n+1)]

def dijkstra(start):
    #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 만든다
    dp[start]=0
    heapq.heappush(heap,(0,start))
    #힙에 원소가 없을떄까지 반복
    while(heap):
        w, now = heapq.heappop(heap)
        #현재 테이블과 비교해서,, 가중치가 더 크다면 무시한다
        if(dp[now]<w):
            continue

        for weight, next_node in nodes[now]:
            next_wei = weight+w
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap,(next_wei,next_node))



for _ in range(m):
    u,v,weight = map(int,input().split())
    nodes[u].append((weight,v))

dijkstra(start_node)

for i in range(1,n+1):
    print("INF" if dp[i]==inf else dp[i])


    

        
        
    
