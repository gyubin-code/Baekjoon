#N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
n = int(input())

nlist =list(map ( int, input().split()))
m = int(input())

mlist = list(map(int,input().split()))

#--------------------------------------------------------------------------
# 이미 정렬 되어있어야한다
nlist = sorted(nlist)
#print(nlist)
#--------------------------------------------------------------------------
left =0
right = n-1

ans =0 #찾고자 하는 수
for i in range(m):
    ans = mlist[i]
    left =0
    right = n-1
    answer =0
    while ( left <= right):
        
        mid = (left+right)//2
        if ans == nlist[mid]:
            answer=1
            
            break
        elif ans < nlist[mid]:
            right = mid-1
        else:
            left = mid+1
    print(answer)
    
        
            


    

