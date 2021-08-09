n =int(input())
#모든 국가를 여행하기 위해서
 
# 0 1 2 3
# 0 2 3 0

for _ in range(n):
    n,m = map (int, input().split())
    nation = [[0 for _ in range(n+1)] for _ in range(n+1)]
    visited =[]
    cnt =0
    for _ in range(m):
        a,b = map(int,input().split())
        
        nation[a][b]=1
        nation[b][a]=1

    start_node =1
    end_node =0
    while len(visited)!=n:
        
        if(start_node not in visited):
            nation[start_node]=end_node
            visited.append(start_node)
            cnt+=1
            start_node=end_node


        
    print(nation)


    #bfs를 공부해 보자
    #이거하려면 , graph[a].append형으로 이루어져있어야 들어갈수있다

    def bfs(graph , start_node):
        visit =list()
        queue =list() #다음으로 방문할 노드

        queue.append(start_node) # 시작 노드를 넣어준다

        while(queue):
            node = queue.pop(0)
            if(node not in visit):
                visit.append(node)
                queue.extend(graph[node]) # 해당노드의 자식들을 큐에 추가해준다

      
        