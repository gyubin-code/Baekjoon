import sys
lambda input: sys.stdin.readline().rstrip

def bfs():
    print('bfs')

def dfs():
    print(dfs)

if __name__ == '__main__':

    #input
    n, m, start = map(int, input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1



