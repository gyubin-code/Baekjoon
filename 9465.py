n=int(input())


def sticker():
    num=int(input())
    a=[]

    for i in range(2):
        a.append(list(map(int, input().split())))
# input()함수로 입력받은 값을 split()로 쪼개고, map함수를 이용하여 int 자료형으로 변환하여 변수 n을 받는다

#print(a)
#a=[[50,10,100,20,40],[30,50,70,10,60]] #예시
#bottle up 으로 생각해보기
# 대각선과 그 전 대각선에 영향을 받는다. 
#각 전대각선 전전 대각선중 더 큰수를 더해가면서 dp를 갱신한다
#하나하나 다 따져가면서 생각하니까 생각보다 쉬웠다 괜히 시간씀 
    a[0][1]+=a[1][0]
    a[1][1]+=a[0][0] #초기값 결정
    for i in range(2,num):
        a[0][i]+=max(a[1][i-1],a[1][i-2])
        a[1][i]+=max(a[0][i-1],a[0][i-2])

 #print(a)
    return max(a[0][num-1],a[1][num-1])

for i in range(n):
    print(sticker())


        
            


    
