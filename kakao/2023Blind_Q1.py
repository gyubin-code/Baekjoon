import collections
def solution(today, terms, privacies):
    answer = []

    ts = collections.defaultdict(int)

    for t in terms:
        i = t.split()
        ts[i[0]] = int(i[1])

    t = today.split('.')
    t_year = int(t[0])
    t_month = int(t[1])
    t_day = int(t[2])
    to = t_year * 365 + t_month * 28 + t_day

    for k, p in enumerate(privacies):
        i = p.split()
        get_time = i[0].split('.')
        _type = i[1]

        years = int(get_time[0])
        month = int(get_time[1])
        day = int(get_time[2])
        add_time = ts[_type]

        total_time = month + add_time

        while total_time > 12:
            years += 1
            total_time -= 12

        month = total_time


        compare = (years) * 365 + (month) * 28 + (day) # 유효기간

        if to >= compare:
            answer.append(k+1)

    print(answer)
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# solution(today, terms, privacies)

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
# solution(today, terms, privacies)

today = "2020.02.01"
terms = ['A 24']
privacies = ['2020.01.01 A']
solution(today, terms, privacies)