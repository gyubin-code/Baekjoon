import collections
#bfs방법을 이용할것이다.
# 1. 0.0 에서 있는길을 넣는다. ( 큐에서 넣을때 카운트를 센다)
# 2. 
#---------------------------------------------------------
# 입력 값 n,m 미로 길 입력
# 4 6
# 101111
# 101010
# 101011
# 111011
n,m =map(int,input().split())
maps_a = list()
maps = list()
for _ in range(n):
    a = str(input())
    maps_a = list()
    for i in range(m):
        maps_a.append(int(a[i]))   
    maps.append(maps_a)    
#---------------------------------------------------------
queue = collections.deque()
queue.append([0,0])
#왼 오 위 아래
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#방문여부도 확인해야해
visit = [[0 for _ in range(m)] for _ in range(n)]
visit[0][0]=1 # 시작은 방문표시
#---------------------------------------------------------
def bfs():
    cnt =0
    while(queue):
        a=queue.popleft()
        x=a.pop(0)
        y=a.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(0<=nx<m and 0<=ny<n and maps[ny][nx]==1 and visit[ny][nx]==0):
                visit[ny][nx]=visit[y][x]+1
                queue.append([nx,ny])
        
    print(visit[n-1][m-1])   

        

    
#---------------------------------------------------------
bfs()