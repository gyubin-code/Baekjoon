n,k,q = map(int,input().split())
arr=[0,0] # 0 1 2 3 4 5 인덱스를 노드들 인덱스 값을 깊이
arr_adult=[0,0] #부모
cnt=1

flag=1+pow(k,cnt)
ans=0
for i in range(2,n+1):
    arr.append(cnt)
    
    if(i==flag):
        cnt+=1
        flag+=pow(k,cnt)

cnt=1

for i in range(2,n+1):
    arr_adult.append(cnt)
    
    if(i==1+k*cnt):
        cnt+=1
              

print(arr)
print(arr_adult)
def sol(arr,arr_adult,q,a,b):
    small_node=0
    small_depth=0
    meet_cnt=0
    
        
        
        #숫자가 더 작은것의 깊이-1의 값 small depth
        #숫자가 더 큰것이  small depth 깊이까지 올라온 경우 부모노드 확인
        # 큰것의 깊이 -  smaill depth 가 큰숫자가 확인해야할 카운트 횟수
        # 임시로 부모 값을 배열을 저장하고, 3번희 횟수만큼 부모노드 갱신
        # 만약 부모노드가 같다면, 1+큰것의 깊이-small depth
        # 만약 부모노드가 다르다면, 각 깊이의 합
    small_node =min(a,b)
       

    small_depth=arr[small_node]-1
    big_node=max(a,b)
    big_depth=arr[big_node]
    meet_adult_cnt=big_depth-small_depth
    tmp_adult=arr_adult
    while(meet_adult_cnt==meet_cnt):
        tmp_adult[big_node]= tmp_adult[tmp_adult[big_node]]

        meet_cnt+=1
    if arr[small_node]==0:
        small_depth=0
    if arr[small_node]==big_depth:
        return 2
    if(arr_adult[small_depth]==tmp_adult[big_depth]):
        return 1+meet_adult_cnt
    else:
        return big_depth+small_depth+1

for i in range(q):
    a,b =map(int,input().split())
    print(sol(arr,arr_adult,q,a,b))
    
     


