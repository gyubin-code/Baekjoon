def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    n = len(routes)
    checked = [0] * n

    for i in range(n):
        if checked[i] == 0:
            camera = routes[i][1] # 진출 지점에 카메라를 갱신
            answer += 1
        for j in range(i+1, n):
            if routes[j][0] <= camera <= routes[j][1] and checked[j] == 0:
                checked[j] = 1
    return answer

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])