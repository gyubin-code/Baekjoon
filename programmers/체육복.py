def solution(n, lost, reserve):
    answer = 0
    visited = [1] * (n+1)
    visited[0] = 0
    lost.sort()
    for r in reserve:
        visited[r] += 1

    for l in lost:
        visited[l] -= 1

    # print(visited)

    for l in lost:
        # 주변 친구들에게 빌리는 경우
        if visited[l] == 0:
            if l-1 in reserve and visited[l-1] > 1:
                visited[l-1] -= 1
                visited[l] += 1
            elif l+1 in reserve and visited[l+1] > 1:
                visited[l+1] -= 1
                visited[l] += 1


    # print(visited)
    for i, v in enumerate(visited):
        if v > 0:
            answer += 1
    # print(answer)
    return answer

solution(5, [4, 2], [1, 3, 5]	)
solution(5, [2, 4], [3]	)
solution(3, [3], [1])
solution(13, [1, 2, 5, 6, 10, 12, 13], [2, 3, 4, 5, 7, 8, 9, 10, 11, 12])