import copy 

def move (position):
    if position ==0: #위로 이동하였을때
        for j in range(n):
            idx =0
            for i in range(1,n):
                if(a[i][j]): # 0이 아닌경우
                    tmp = a[i][j]
                    a[i][j]=0
                    if(a[idx][j]==0):#빈칸이기 떄문에 옮긴다. 나중에 합쳐질수도 있기 때문에 IDX는 변경하지 않는다
                        a[idx][j]=tmp
                    elif a[idx][j]==tmp:#같은 값이라면, 2배로 만들고 합친블럭은 다시 합칠수없기때문에 idx를 증가시킨다
                        a[idx][j]=tmp*2
                        idx+=1
                    else: #이외의 다른 값이라면, 그 위에 쌓아야하기 떄문에 인덱스를 증가시킨후에 블럭을 옮긴다.
                        idx+=1
                        a[idx][j]=tmp
    elif position ==1: #아래로 이동하였을때
        for j in range(n):
            idx =n-1
            for i in range(n-2,-1,-1):
                if(a[i][j]): # 0이 아닌경우
                    tmp = a[i][j] #그 아래 있는 값보다 하나 위의값
                    a[i][j]=0
                    if(a[idx][j]==0):#빈칸이기 떄문에 옮긴다. 나중에 합쳐질수도 있기 때문에 IDX는 변경하지 않는다
                        a[idx][j]=tmp
                    elif a[idx][j]==tmp:#같은 값이라면, 2배로 만들고 합친블럭은 다시 합칠수없기때문에 idx를 증가시킨다
                        a[idx][j]=tmp*2
                        idx-=1
                    else: #이외의 다른 값이라면, 그 위에 쌓아야하기 떄문에 인덱스를 증가시킨후에 블럭을 옮긴다.
                        idx-=1
                        a[idx][j]=tmp
    elif position ==2: #좌측으로 이동시킬때
        for i in range(n):
            idx =0
            for j in range(1,n):
                if(a[i][j]): # 0이 아닌경우
                    tmp = a[i][j]
                    a[i][j]=0
                    if(a[i][idx]==0):#빈칸이기 떄문에 옮긴다. 나중에 합쳐질수도 있기 때문에 IDX는 변경하지 않는다
                        a[i][idx]=tmp
                    elif a[i][idx]==tmp:#같은 값이라면, 2배로 만들고 합친블럭은 다시 합칠수없기때문에 idx를 증가시킨다
                        a[i][idx]=tmp*2
                        idx+=1
                    else: #이외의 다른 값이라면, 그 위에 쌓아야하기 떄문에 인덱스를 증가시킨후에 블럭을 옮긴다.
                        idx+=1
                        a[i][idx]=tmp

    elif position ==3:
        for i in range(n):
            idx =n-1
            for j in range(n-2,-1,-1):
                if(a[i][j]): # 0이 아닌경우
                    tmp = a[i][j]
                    a[i][j]=0
                    if(a[i][idx]==0):#빈칸이기 떄문에 옮긴다. 나중에 합쳐질수도 있기 때문에 IDX는 변경하지 않는다
                        a[i][idx]=tmp
                    elif a[i][idx]==tmp:#같은 값이라면, 2배로 만들고 합친블럭은 다시 합칠수없기때문에 idx를 증가시킨다
                        a[i][idx]=tmp*2
                        idx-=1
                    else: #이외의 다른 값이라면, 그 위에 쌓아야하기 떄문에 인덱스를 증가시킨후에 블럭을 옮긴다.
                        idx-=1
                        a[i][idx]=tmp
def dfs(cnt):
    global a, ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                
                ans = max(ans,a[i][j])
            
        return
    
    tmp_a = copy.deepcopy(a)
    for i in range(4):
        move(i)
        dfs(cnt+1)
        a = copy.deepcopy(tmp_a)
        
                
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]            
ans =0
dfs(0)
print(ans)

    

        
    