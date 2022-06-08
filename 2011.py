import sys

lambda input: sys.stdin.readline().rstrip




if __name__ =='__main__':

    # top - down
    arr = list(map(int, input()))
    dp = list()
    dp = [0 for _ in range(len(arr)+1)]

    dp[0], dp[1] = 1, 1

    if arr[0] == 0:
        print(0)
    else:
        for i in range(2, len(arr)+1): #i는 자릿수
            compareLen = arr[i-1] + (10* arr[i-2])
            # print(compareLen)
            if arr[i-1] > 0:
                dp[i] += dp[i-1]
            if 9 < compareLen < 27: # 그 사이의 숫자가 있다면
                dp[i] += dp[i-2]

        print(dp[len(arr)] % 1000000)








