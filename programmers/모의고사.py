import collections


def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    correct = [[0] * 10 for _ in range(3)]

    for i, a in enumerate(answers):
        if one[i % len(one)] == a:
            correct[0][i] = 1

        if two[i % len(two)] == a:
            correct[1][i] = 1

        if three[i % len(three)] == a:
            correct[2][i] = 1

    c = [0,0,0]
    d = collections.defaultdict(list)
    for i in range(3):
        d[sum(correct[i])].append(i+1)
    m = 0
    for i in d.keys():
        m = max(m, i)




    return d[m]

solution([1,2,3,4,5])
solution([1,3,2,4,2])