import collections


def solution(orders, course):
    import itertools
    answer = []

    for c in course:
        combs = list()
        d = collections.defaultdict(int)
        # combs 생성
        for order in orders:
            comb = list(itertools.combinations(sorted(order), c)) # 한 손님이 만들수 있는 2개의 콤비네이션 생성
            combs.extend(comb)

        for comb in combs:
            comb_str = ''.join(comb)
            d[comb_str] += 1


        for i in d:
            if d[i] == max([ d[order] for order in d ] ):
                if d[i] > 1:
                    answer.append(i)

    print(sorted(answer))
    return sorted(answer)

# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4] )
solution(["XYZ", "XWY", "WXA"], [2,3,4])