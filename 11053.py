#하다가 꺼져서 맞겠거니 하고 올렸는데 다시 키니까 런타임 에러떠서 입력부분+ for구간 변경함
num = int(input())
Arr = list(map(int, input().split())) #이부분 구글링참고
# print(Arr)
dp=[1]*num

for i in range(0,num):
    for j in range(i):
        if(Arr[j]<Arr[i]):
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))