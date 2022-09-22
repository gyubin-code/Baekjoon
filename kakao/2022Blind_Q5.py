

def solution(info, edges):
    visited = [0] * len(info)
    visited[0] = 1
    answer = []

    def dfs(s, w):
        if s > w:
            answer.append(s)
        else:
            return

        for i in range(len(edges)):
            p = edges[i][0]
            c = edges[i][1]
            is_wolf = info[c]

            if visited[p] and not visited[c]:
                visited[c] = 1
                if is_wolf == 1:
                    dfs(s, w+1)
                else:
                    dfs(s+1, w)
                visited[c] = 0

    dfs(1, 0)

    print(max(answer))
    return max(answer)


solution([0,0,1,1,1,0,1,0,1,0,1,1],	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])