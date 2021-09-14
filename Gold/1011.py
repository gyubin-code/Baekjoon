n= int(input())


def solve(k):
    dist = k[1]-k[0]

    
    turn=1
    pos =1
    pos_pow=0
    while(pos<dist):
        pos_pow+=1
        turn+=1
        pos+=pos_pow
        if(pos>=dist):
            break;
        turn+=1
        pos+=pos_pow
        if(pos>=dist):
            break;
    
    if(pos>dist):
        turn-=1
    print(turn)

for i in range(n):
    k = list(map(int,input().split(" ")))
    solve(k)