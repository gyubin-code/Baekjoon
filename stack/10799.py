import sys

pip = list(map(str,sys.stdin.readline()))
i=0
cnt=0
stick=0
while(i<len(pip)-1):
    if pip[i]=='(' and pip[i+1]==')': #레이저인경우
        cnt+=stick
        i+=2
    elif pip[i]=='(':
        stick+=1
        i+=1
    else:
        cnt+=1 # 레이저가 아닌 )인경우 , 레이저와 별개로 조각이 생겨난다.
        stick-=1
        i+=1

    

print(cnt)