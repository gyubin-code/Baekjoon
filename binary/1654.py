import sys
lambda input: sys.stdin.readline().rstrip

def solve(arrs: list, n :int ):
    start = 1
    end = max(arrs)
    while(start <= end):
        cnt = 0 #
        mid = (start + end) // 2

        for arr in arrs:
            cnt += (arr//mid)

        if cnt < n:
            end = mid-1
        else:
            start = mid+1

    print(end)
if __name__ == '__main__':
    k, n = map(int, input().split())

    arr = list()

    for _ in range(k):
        arr.append(int(input()))

    solve(arr, n)