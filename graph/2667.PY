import collections
# 토마토 문제에ㅣ 있는걸 그대로 가져왔다 변형해서 사용할것
n = int(input())
maps = []
for i in range(n):
    maps.append(list(map(int, input())))    
#---------------------------------------------------------
queue = collections.deque()
#왼 오 위 아래
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#방문여부도 확인해야해
visit = [[0 for _ in range(n)] for _ in range(n)]
home_num =[]
home_cnt =0
#---------------------------------------------------------
def bfs():
    cnt=0
    while(queue):
        a=queue.popleft()
        
        x=a.pop(0)
        y=a.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(0<=nx<n and 0<=ny<n and visit[ny][nx]==0 and maps[ny][nx]==1):
                visit[ny][nx]=1
                queue.append([nx,ny])
                cnt+=1
              
    return cnt+1



#---------------------------------------------------------
for i in range(n):#y
    for j in range(n):#x
        if(maps[i][j]==1 and visit[i][j]==0):
            visit[i][j]=1
            queue.append([j,i])
            home_num.append(bfs())
            home_cnt+=1

home_num.sort()
print(home_cnt)
for i in range(home_cnt):
    print(home_num[i])

        

    
#---------------------------------------------------------
