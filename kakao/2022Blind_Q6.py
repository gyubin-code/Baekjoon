def solution(n, info):
    import itertools
    answer = [-1]
    gap = -1

    for comb in itertools.combinations_with_replacement(range(11), n):
        # 1~ 10 까지 중복을 허용하여, N개 뽑는다
        info2 = [0] * 11

        for i in comb:
            info2[10-i] += 1

        a, l = 0, 0
        for i in range(11):
            if info[i] == info2[i] == 0: # 라이언 어피치 둘다 없음
                continue

            elif info[i] >= info2[i]: # 어피치가 더 맞춘경우
                a += 10 - i

            else: # 라이언이 맞춘경우
                l += 10 - i

        if l > a:
            g = l - a
            if g > gap:
                gap = g
                answer = info2

    print(answer)
    return answer

solution(5, [2,1,1,1,0,0,0,0,0,0,0])
# solution(1,	[1,0,0,0,0,0,0,0,0,0,0])
# solution(9, [0,0,1,2,0,1,1,1,1,1,1])



