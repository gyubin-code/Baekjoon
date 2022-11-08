def solution(users, emoticons):

    import itertools, math
    answer = []

    len_e = len(emoticons)

    mr = [0, 0]

    for comb in itertools.product([10, 20, 30, 40], repeat=len_e):

        re1 = 0
        re2 = 0
        for u in users:
            total = 0
            # 개개인 계산
            for i, c in enumerate(comb):
                if c >= u[0]:
                    # 산다
                    total += emoticons[i] * (100-c)/100 # 해당 이모티콘을 얼마에 할인된 가격에 산건지 측정

            if total >= u[1]:
                re1 += 1
            else:
                re2 += total # 이모티콘 플러스 안사는 경우에는 총액 더하기

        if re1 > mr[0]:
            mr[0] = re1
            mr[1] = math.floor(re2)
        if re1 == mr[0] and re2 > mr[1]:
            mr[0] = re1
            mr[1] = math.floor(re2)
        # answer.append([re1, math.floor(re2)])

    # answer.sort(key=lambda x: (-x[0], -x[1]))
    print(mr)
    return mr

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
solution(users, emoticons)

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
solution(users, emoticons)