def solution(sizes):
    for i in range(len(sizes)):
        if i == len(sizes) -1 :
            break
        if max(sizes[i][0], sizes[i+1][0]) * max(sizes[i][1], sizes[i+1][1]) > max(sizes[i][0], sizes[i+1][1]) * max(sizes[i][1], sizes[i+1][0]):
            sizes[i+1][0], sizes[i+1][1] = max(sizes[i][0], sizes[i+1][1]), max(sizes[i][1], sizes[i+1][0])
        else:
            sizes[i+1][0], sizes[i+1][1] = max(sizes[i][0], sizes[i+1][0]) , max(sizes[i][1], sizes[i+1][1])
    answer = sizes[len(sizes)-1][0] * sizes[len(sizes)-1][1]
    return answer
solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])