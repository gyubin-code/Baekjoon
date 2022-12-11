def make_board(subway):
    subways = []
    cnt = 0
    for s in subway:
        tmp = list(map(int, s.split()))
        subways.append(tmp)
        cnt = max(cnt, len(tmp))
    return subways, cnt
def solution(subway, start, end):
    answer = 0
    subway, cnt = make_board(subway)
    visited = [[0] * cnt for _ in range(len(subway))]
    for j in range(len(subway)):
        for i in range(len(subway[j])):

            if visited[j][i] == 0 and

    return answer

solution(["1 2 3 4 5 6 7 8", "2 11", "0 11 10", "3 17 19 12 13 9 14 15 10", "20 2 21"], 1, 9)