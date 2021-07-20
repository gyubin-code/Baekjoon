#화살의 이동경로를 flag에 기록하였다. 
#화살의 존재여부에 대한 확인이 제일 중요하였다
#이걸 몰라서 많이 헤맴
n = int(input())
ballons =list(map(int,input().split()))

flag =[0]*10000001

ans = 0

for i in range(len(ballons)):
    if(flag[ballons[i]]==0):
        ans +=1
        flag[ballons[i]-1]+=1
    else:
        flag[ballons[i]]-=1
        flag[ballons[i]-1]+=1
print(ans)