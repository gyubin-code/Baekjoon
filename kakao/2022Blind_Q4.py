def solution(id_list, report, k):
    answer = []
    import collections

    r_list = []
    d = collections.defaultdict(list)

    for i in id_list:
        d[i]

    report = list(set(report))

    r_b = []
    for r in report:
        t = r.split()
        r_list.append(t)
        r_b.append(t[1])
        d[t[0]].append(t[1])

    ban_dict = collections.Counter(r_b)
    ban_list = []

    for key, v in ban_dict.items():
        if v >= k:
            ban_list.append(key)

    for k, v in d.items():
        cnt = 0
        for i in v:

            if i in ban_list:
                cnt += 1

        answer.append(cnt)

    print(answer)
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]

solution(id_list, report, 2)

solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
