# 수열 출력하기
n, m  = map(int, input().split())

# 숫자 n까지 사용하여 길이가m인 수열 출력하기

arr = [0] * 10
is_used = [False] * 10


def func(k: int):
    # k 배열 위치
    if k == m:
        for i in range(m):
            print(arr[i], end = " ")
        print()
        return

    for i in range(1, n+1):
        if not is_used[i]:
            is_used[i] = True
            arr[k] = i
            func(k+1)
            is_used[i] = False # 위 func이 끝나면 사용한거 취소

func(0)