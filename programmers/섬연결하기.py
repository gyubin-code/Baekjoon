import heapq

def find_parent(parent, x):
    # 특정 원소가 속한 집합 찾기
    # 재귀
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_child(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b



def solution(n, costs):
    answer = 0
    q = []
    parent = [0] * n

    for i in range(n):
        parent[i] = i

    for c in costs:
        heapq.heappush(q, [c[2], c[0], c[1]]) # w t f

    while q:
        w, t, f = heapq.heappop(q)

        if find_parent(parent, t) != find_parent(parent, f):
            union_child(parent, t, f)
            answer += w

    # print(answer)

    return answer

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
