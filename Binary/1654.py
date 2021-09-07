import sys
n, k = map ( int, input().split())
line = [int(sys.stdin.readline()) for _ in range(n)]
start, end = 1,max(line)

while(start <=end):
    mid = (start+end)//2 
    lines = 0 # 랜선갯수
    
    for i in line:
        lines += i // mid  #  분할된 랜선 수
    
    if lines>=k:
        start = mid+1
    else:
        end = mid-1

print(end)