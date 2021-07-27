a,b = map(int,input().split())
arr =[[0]*(b+1) for _ in range(a+1)]



arr = [list(map(str, input())) for _ in range(1,a+1)]


def find(arr, i,b):
    cnt=-1
    for m in range(b):
        if(arr[i][m]=="c"):
            cnt=0
            
            arr[i][m]=0
        else: #.인경우에는
            if(cnt==-1): #이전에 구름이 없던경우
                arr[i][m]=-1
            else: 
                cnt+=1
                arr[i][m]=cnt

            
            

for i in range(a):
    find(arr,i,b)
for i in range(a):
    for j in range(b):
        print(arr[i][j],end=' ')
    print()

    
        





    