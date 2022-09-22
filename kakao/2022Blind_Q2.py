def cal(t1, t2):

    l1 = t1.split(":")
    l2 = t2.split(":")

    return ((int(l2[0]) * 60 + int(l2[1])) - (int(l1[0]) * 60 + int(l1[1])))

def solution(fees, records):
    import math, collections
    answer = []
    cars = collections.defaultdict(int) # 차
    r_list = []

    for r in records:
        r = r.split()
        r_list.append(r)

    r_list.sort(key=lambda x: (x[1], x[0], x[2]))

    for i in range(len(records)-1):
        r1 = r_list[i]
        r2 = r_list[i+1]

        # 입차 + 탈차 -> 번호 체크
        if r1[1] == r2[1] and r1[2] == 'IN' and r2[2] == 'OUT':
            cars[r1[1]] += cal(r1[0], r2[0])

        # 입차만 한경우
        if r1[1] != r2[1] and r1[2] == 'IN':
            cars[r1[1]] += cal(r1[0], "23:59")

    if r_list[len(records) - 1][2] == 'IN':
        cars[r_list[len(records)-1][1]] += cal(r_list[len(records)-1][0], "23:59")

    for v in cars.values():
        if v <= fees[0]:
            answer.append(int(fees[1]))
        else:
            answer.append(int(fees[1] + math.ceil((v-fees[0])/fees[2]) * fees[3]))

    print(answer)
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

solution(fees, records)

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

solution(fees, records)

fees= [1, 461, 1, 10]
records = ["00:00 1234 IN"]

solution(fees, records)