
def token(query: str):
    import collections
    tokens = query.split()
    ts = []
    for t in tokens:
        if t == 'and' or t == '-':
            continue
        ts.append(t)

    return sorted(ts, reverse=True)
def solution(info, query):
    answer = []
    infos = []
    querys = []
    for i in info:
        infos.append(token(i))

    for i in query:
        querys.append(token(i))

    for query in querys:
        cnt = 0
        for info in infos:
            i = len(set(query[:-1]) - set(info[:-1]))
            if i <= 0 and int(query[-1]) <= int(info[-1]):
                cnt += 1
        answer.append(cnt)

    print(answer)
    return answer
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])