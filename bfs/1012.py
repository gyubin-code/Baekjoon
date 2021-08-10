T = int(input()) #테스트 케이스 갯수


max_x = 50
max_y = 50

#bfs한번당 한 섹션을 찾는것
def bfs(cavege,visit,x,y,m,n,cnt):
    # 양옆좌우 확인하기
    # 위 오른 아래 왼
    dx =[-1,0,1,0]
    dy =[0,1,0,-1]
    #들어왔을때는 방문확인부터 넣기
    
    queue_x =list() # 초기 위치는 넣어두기
    queue_y=list()
    
    queue_x.append(x)
    queue_y.append(y)

    #좌우방문 확인하기
    #큐가 빌때까지 확인하기
    
    
    while(1):
        if not queue_x:
            
            break
        else:
            q_x=queue_x.pop(-1)
            q_y=queue_y.pop(-1)
            for i in range(4):
                nx =q_x+dx[i]
                ny =q_y+dy[i]
                
                #일단 위치가 위 오른 아래 왼이 범위에서 벗어나면 안돼
                if(nx>=0 and nx<=(m-1) and ny >= 0 and ny <=(n-1)):
                    # 양배추가 있는데, 방문하지 않은 경우라면, 표시하고, 큐에 넣고, 큐에서 뺀거를 사용,,!
                    if(cavege[ny][nx]==1 and visit[ny][nx]==0):
                        visit[ny][nx]=1
                        queue_x.append(nx)
                        queue_y.append(ny)
                        
            


    
    return cnt+1
    
    # 케이스가 돌아갈때마다 새로 선언 시켜서 bfs에 넣기
for _ in range(T):
    m,n,k = map(int, input().split()) #가로 , 세로, 양배추 개수
    cavege = [[0 for _ in range(m)] for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        cavege[y][x] = 1

        #완전 탐색으로 하나하나 확인하면서 방문확인하기
    for j in range(n): # y
        for i in range(m):  # x  
                # 양배추는 있는데, 방문하지 않은 양배추인경우
            if(cavege[j][i] == 1 and visit[j][i] == 0):
                visit[j][i] = 1
                cnt =bfs(cavege, visit, i, j, m, n,cnt)
                
                # print(bfs(cavege, visit, i, j, m, n))
                    # #방문 양배추 갱신
                    # visit = bfs(cavege, visit, i, j, m, n)
    # print(visit)
    print(cnt)




