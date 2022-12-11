import collections


def day2time(time):
    # 00:02:05:18 -> 0000:00:00:02:05:18
    tmp = [0,0]
    res = tmp + list(map(int, time.split(':')))
    return res


def cal(t1, t2):
    tmp = 0
    res = collections.deque()

    s = t1[5] + t2[5]
    if s > 59:
        tmp = 1
        s -= 60
    res.appendleft(s)

    m = t1[4] + t2[4] + tmp
    tmp = 0
    if m > 59:
        tmp = 1
        m -= 60
    res.appendleft(m)

    h = t1[3] + t2[3] + tmp
    tmp = 0
    if h > 23:
        tmp = 1
        h -= 24
    res.appendleft(h)

    d = t1[2] + t2[2] + tmp
    tmp = 0
    if d > 30:
        tmp = 1
        d -= 30
    res.appendleft(d)

    m = t1[1] + t2[1] + tmp
    tmp = 0
    if m > 12:
        tmp = 1
        m -= 12
    res.appendleft(m)

    y = t1[0] + t2[1] + tmp
    res.appendleft(y)

    return res


def minor(t1, t2):
    return (t1[0] - t2[0]) * 360 + (t1[1] - t2[1]) * 30 + t1[2] - t2[2] + 1


def solution(s, times):
    res = 0
    start = list(map(int, s.split(':')))
    s = [start[0], start[1], start[2]]

    fund = []
    fund.append([start[0], start[1], start[2]])

    # 년 월 일 시간 분 초
    for t in times:
        time = day2time(t)
        start = cal(start, time)
        if [start[0], start[1], start[2]] not in fund:
            fund.append([start[0], start[1], start[2]])

    cnt = minor([start[0], start[1], start[2]], s)

    if cnt == len(fund):
        res = 1

    answer = [res, cnt]
    print(answer)
    return answer

solution("2021:04:12:16:08:35", ["01:06:30:00", "01:04:12:00"])
solution("2021:04:12:16:08:35", ["00:01:12:00", "00:01:12:00", "00:01:12:00"])
solution("2021:12:12:16:08:35",["99:23:59:59"])
solution("2021:04:12:16:08:35", ["01:06:30:00", "01:01:12:00", "00:00:09:25"])

