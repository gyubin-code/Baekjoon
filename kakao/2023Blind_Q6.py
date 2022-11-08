def solution(cap, n, deliveries, pickups):
    answer = -1

    # 한번 왕복시에 최대의 효율이 나는것
    m_len = 5
    while 1:

        for i in range(1, n):
            if sum(deliveries[i:m_len]) <= cap:
                if sum(pickups[i:m_len]) <=
    return answer