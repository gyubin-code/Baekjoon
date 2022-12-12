answer = -1
def solution(N, number):
    global answer

    def dfs(N, number, cnt, prev):
        global answer
        # n의 카운트를 늘려가며 dfs
        #  그 값을 저장하고 number와 동일한지 확인
        tmp_n = N
        if cnt > 8:
            answer = -1
            return
        if number == prev:
            if answer == -1 or answer > cnt:
                answer = cnt
            return

        for i in range(8-cnt):
            dfs(N, number, cnt+i+1, prev+tmp_n)
            dfs(N, number, cnt+i+1, prev-tmp_n)
            dfs(N, number, cnt+i+1, prev*tmp_n)
            dfs(N, number, cnt+i+1, prev/tmp_n)
            tmp_n = tmp_n * 10 + N

    dfs(N, number, 0, 0)
    return answer

print(solution(5, 12))


