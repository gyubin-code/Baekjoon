import sys
read=sys.stdin.readline
card =read()
arr=[[] for _ in range(4)]
answer=[]

#card[i+1]+card[i+2]

for i in range(0,len(card)-3,3):
    
    a= int(card[i+1])*10+int(card[i+2])

    if(card[i] =='P'):
        arr[0].append(a)
    if(card[i] =='K'):
        arr[1].append(a)
    if(card[i] =='H'):
        arr[2].append(a)
    if(card[i] =='T'):
        arr[3].append(a)

def sol(arr):
    for i in range(4):
        if(len(arr[i])!=len(set(arr[i]))):
                return print("GRESKA")
        else:
            answer.append(13-len(arr[i]))
    for i in range(4):
        print(answer[i],end=' ');


sol(arr)



        
        
    