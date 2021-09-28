import sys,copy,itertools
read = sys.stdin.readline
n,m = map(int,read().split())
maps=[]
for _ in range(n):
    maps.append(list(map(int,sys.stdin.readline().split())))

home =[]
chicken =[]
for i in range(n):
    for j in range(n):
        if(maps[i][j]==2):# chicken
            chicken.append((i,j))
        if maps[i][j]==1: #home
            home.append((i,j))


com_chicken =list(itertools.combinations(chicken,m))
result = [0]*len(com_chicken)

for i in home:
    for j in range(len(com_chicken)):
        infi = sys.maxsize
        for k in com_chicken[j]:
            length = abs(i[0]-k[0])+abs(i[1]-k[1])
            infi = min(infi,length)
        result[j]+=infi

print(min(result))
