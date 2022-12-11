import itertools


def solution(k, dungeons):
    answer = -1
    init_k = k
    for comb in itertools.permutations(dungeons, len(dungeons)):
        array = list(comb)
        k = init_k
        res = 0
        for a in array:
            if k >= a[0]:
                k -= a[1]
                res += 1
        answer = max(answer, res)

    # print(answer)
    return answer


solution(80, [[80,20],[50,40],[30,10]])