import collections 
m,n = map(int,input().split())
tomatos = []
dx =[-1,0,1,0]
dy =[0,1,0,-1]
ans =0
#--------------------------------------------------------------
for i in range(n): #y
    tomatos.append(list(map(int,input().split())))
#--------------------------------------------------------------
# bfs이용하여 풀기
#--------------------------------------------------------------
# 일단 ! 기존 토마토 넣기
queue = collections.deque()
for i in range(n): #y
    for j in range(m): # x
        if(tomatos[i][j]==1):
            queue.append([j,i])#(x,y)삽입
#--------------------------------------------------------------

def bfs():
    
    while(queue):
        a=queue.popleft() #[x,y] 뽑기
        
        x=a.pop(0)
        y=a.pop(0)
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if(0<=nx<m and 0<=ny<n and tomatos[ny][nx]==0 ):
                
                queue.append([nx,ny])
                
                tomatos[ny][nx]=tomatos[y][x]+1
                
                
                
    
    


#--------------------------------------------------------------
bfs()

#--------------------------------------------------------------
for i in tomatos:
    for j in i:
        if j ==0:
            print(-1)
            exit(0)
    ans = max(ans , max(i))

print(ans-1)