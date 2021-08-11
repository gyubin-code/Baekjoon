import sys     
sys.setrecursionlimit(10000)
# 시간복잡도가 틀린것이 아니기 때문에 recursive 한도를 풀어주었고, pypy를 통해 품
T = int(input()) #테스트 케이스 갯수 


max_x = 50
max_y = 50

#bfs한번당 한 섹션을 찾는것
def dfs(cavege,visit,stack_x,stack_y,cnt,m,n):
    # 양옆좌우 확인하기
    # 위 오른 아래 왼
    dx =[-1,0,1,0]
    dy =[0,1,0,-1]
    #들어왔을때는 방문확인부터 넣기
    # 맨 위에있는 스택을 쓸건데, 일단 방문표시
    visit[stack_y[-1]][stack_x[-1]]=1
    
           
    #빈 스택이 아닌경우
     # 첨에 스택에서 뽑고,  그 해당스택에서의 배추가 있는인접되는 노드 값들을 넣을 다음에  
    # 제일 위에 있는 값을 뽑아서 뽑은값이 방문을 했을 시에는 첨으로돌아감(계속방문하면 스택이 언젠간 끝남), 방문을 안했을 시에는 방문 표시를 하고 돌아가기 그리고 
    
    tmp_x = stack_x.pop()
    tmp_y = stack_y.pop()
    for i in range(4):
        #만약 cavege가 있는경우는 모두 넣는다.
        #리스트의 범위가 벗어나지 않는 한에서 양배추가있고 방문하지 않았다면 스택에 넣는다
        if(tmp_y+dy[i]>=0 and tmp_y+dy[i]<n and tmp_x+dx[i]>=0 and tmp_x+dx[i]<m):
            if(cavege[tmp_y+dy[i]][tmp_x+dx[i]]==1 and visit[tmp_y+dy[i]][tmp_x+dx[i]]==0):
                stack_x.append(tmp_x+dx[i])
                stack_y.append(tmp_y+dy[i])
    # 뽑고보니 마지막 노드였던 경우 ! 
    if(not stack_x): # 마지막 노드인경우
        return 1
    # 아직 스택에 값이 남아있는경우
    else: #노드가 남아있는경우, 
        return dfs(cavege,visit,stack_x,stack_y,cnt,m,n)
    
    
    # 케이스가 돌아갈때마다 새로 선언 시켜서 bfs에 넣기
for _ in range(T):
    m,n,k = map(int, input().split()) #가로 , 세로, 양배추 개수
    cavege = [[0 for _ in range(m)] for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    stack_x= list()
    stack_y=list()

    for _ in range(k):
        x, y = map(int, input().split())
        cavege[y][x] = 1

        #완전 탐색으로 하나하나 확인하면서 방문확인하기
    for j in range(n): # y
        for i in range(m):  # x  
                # 양배추는 있는데, 방문하지 않은 양배추인경우
            if(cavege[j][i] == 1 and visit[j][i] == 0):
                visit[j][i] = 1
                stack_x.append(i)
                stack_y.append(j)
                cnt +=dfs(cavege, visit, stack_x, stack_y,cnt,m,n)
                
                # print(bfs(cavege, visit, i, j, m, n))
                    # #방문 양배추 갱신
                    # visit = bfs(cavege, visit, i, j, m, n)
    # print(visit)
    print(cnt)




