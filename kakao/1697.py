import collections


n, k = map(int, input().split())
m_len = 100000 + 1
visited = [0] * m_len
q = collections.deque()

q.append(n)

def bfs():
    while q:
        l = q.popleft()
        a = l + 1
        b = l - 1
        c = l * 2

        if a == k or b == k or c == k:
            return visited[l] + 1

        # 범위, 방문, 조건
        if a < m_len and visited[a] == 0:
            visited[a] = visited[l] + 1
            q.append(a)

        if b >= 0 and visited[b] == 0:
            visited[b] = visited[l] + 1
            q.append(b)

        if 0 <= c < m_len and visited[c] == 0:
            visited[c] = visited[l] + 1
            q.append(c)

    return visited[k] + 1

if n == k:
    print(0)
else:
    print(bfs())



