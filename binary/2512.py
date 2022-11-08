import sys
n = int(input())
k = list(map(int,sys.stdin.readline().split()))
total_money = int(input())
start = 1
end = max(k)
tmp_total_money=0
while(start<=end):
    
    tmp_total_money=0
    mid = (start+end)//2 
    
    for i in k:
        if(i>=mid):
            tmp_total_money+=mid
            
        else:
            tmp_total_money+=i
             
    if tmp_total_money>total_money: #예상값이 더 큰 경우
        end =mid-1
    else: 
        start=mid+1
    if(start>end):
        print(end)
    
        
