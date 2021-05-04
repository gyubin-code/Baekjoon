import sys
num=int(sys.stdin.readline())
Arr = list(map(int, sys.stain.readline().split())) #이게몰가ㅏㅏㅏㅏ 리스트 받는법을 공부해야겟다 이부분 구글링참고
# print(Arr)
dp=[1]*num

for i in range(1,num):
    for j in range(i):
        if(Arr[j]<Arr[i]):
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))