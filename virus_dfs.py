from sys import stdin
read =stdin.readline #한줄단위로 받는것이당 \n포함
com_num=int(read())
edge=int(read())
dic ={}# set을 만들기 위한 자료형이다
visited=[] # 큐

for i in range(com_num):
    dic[i+1]=set()

for i in range(edge):
    a,b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start,dic):
    for i in dic[start]:
        if i not in visited:#처음 와봤을때
            visited.append(i)
            
            dfs(i,dic)



dfs (1, dic)
print(len(visited)-1)
