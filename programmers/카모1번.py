def solution(flowers):
    answer = 0
    long_day = 0
    for f in flowers:
        long_day = max(max(f), long_day)
    visited = [0] * long_day

    for f in flowers:
        for i in range(f[0], f[1]):
            visited[i] = 1

    print(visited)
    print(sum(visited))
    return sum(visited)

solution([[2, 5], [3, 7], [10, 11]])
solution([[3, 4], [4, 5], [6, 7], [8, 10]])
solution([[1, 364], [2, 365]])