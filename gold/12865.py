#dp 를 사용,, 
#dp = 1 은 무게 마다 더 큰 값을 갱신하는 방법을 사용하자,, !
#최적의 원리란 어떤 문제의 입력사례의 최적해가 그 입력사례를 분할한 부분사례에 대한 최적해를 포함한다면, 항상 그 문제으 ㅣ최적의 사례를 성립한다
n,k = map(int,input().split())
wt =[]
val=[]

for i in range(n):
    w,v = map(int,input().split())
    wt.append(w)
    val.append(v)


def knapsack(w,wt,val,n): # w 배낭의 한도, wt, 각 보석의 무게, val 각 보석의 가격, n 보석의 수
    k = [[0 for x in range(w+1)]for y in range(n+1)]
    for i in range(n+1):
        for w in range(w+1):
            if(i==0 or w==0):
                k[i][w]=0
            elif wt[i-1]<=w: #받은 무게가 한도보다 작은경우
                k[i][w]=max(val[i-1]+k[i-1][w-wt[i-1]], k[i-1][w])    
            else: #한도보다 크다면 2차원 배열에서의 위에값을 가져온다
                k[i][w]=k[i-1][w]
    
    return k[n][w]

print(knapsack(k,wt,val,n))