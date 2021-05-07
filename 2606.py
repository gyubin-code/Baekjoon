#알고리즘 복습용 bfs 문제 예시 
#adj라는 2차원 배열을 선언한뒤 연결 을 나타낸다 
#ex> adj[2]=[1,3,4]  배운대로 구현하는게 제일 어려웠음 잊지말기(line10-13)

comnum=int(input())
link=int(input())
adj = [[] for _ in range(comnum + 1)]
visited = [False] * (comnum + 1)  
count=0 
for _ in range(link):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
    
def dfs(now_pos):
    global count
    count+=1
    visited[now_pos] = True
    for next_pos in adj[now_pos]:
        if not visited[next_pos]:
            dfs(next_pos)
    
dfs(1)
print(count - 1)


