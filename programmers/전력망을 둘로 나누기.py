import itertools, collections

def bfs(graph, node, visited):
    # 큐 구현을 위한 deque 라이브러리 활용
    queue = collections.deque([node])
    # 현재 노드를 방문 처리
    visited[node] = 0

    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        v = queue.popleft()
        # 탐색 순서 출력
        # print(v, end=' ')
        # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = 1

    return visited


def solution(n, wires):
    answer = 1e9
    wires_n = len(wires) - 1
    for comb in itertools.combinations(wires, wires_n):
        visited = [0] * (n+1)
        board = [[] for _ in range(n+1)]
        for c in comb:
            board[c[0]].append(c[1])
            board[c[1]].append(c[0])

        visited = bfs(board, 1, visited)
        answer = min(answer, abs((n-sum(visited)) - sum(visited)))
    # print(answer)
    return answer

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])