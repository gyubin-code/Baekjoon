from collections import deque
import sys     
sys.setrecursionlimit(10000)
n, k =map(int, input().split())
visited =[False]*100001
depth =[0]*20



def bfs(n):
    count = 0
    q = deque([[n, count]])
    while q:
        v = q.popleft()
        e = v[0]
        count = v[1]
        if not visited[e]:
            visited[e] = True
            if e == k:
                return count
            count += 1
            if (e * 2) <= 100000:
                q.append([e * 2, count])
            if (e + 1) <= 100000:
                q.append([e + 1, count])
            if (e - 1) >= 0:
                q.append([e - 1, count])
       

        


        

print(bfs(n))   
