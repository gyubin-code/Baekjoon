# 네이버에 "특정 금액 계산 백준" 이라고 침
# 결과를 토대로 동적 계획법이 나옴
# 대표적 문제는 4개이다
# Assembly-line schduling, rod cutting , lcs, matrix-chain multiplication
# 어떤 문제에 대한 "최적해를 얻고자 하는것 "
# 알고리즘 대회에서 가장 문제의 양이 많다.
# 중요 예시는 url : https://www.leafcats.com/71
# 계산한 작은 문제 -> 큰 문제 해결 ex) fn = fn-1+fn-2
# 현재 문제에서 보내주는 방식 ( 앞으로 해결할 문제에 보내주는 방식) //먼소리야
# 메모이제이션, 계산




price = int(input())
dp = [0]*(price+1) #주소를 개수를 맞춰서 놓기
dp[0]=1
k = int(input())
for i in range(k):
    a,b= map (int, input().split())
    for price_num in range(price,0,-1):
        for k in range(1,b+1):
            if(price_num-a*k<0): break;
            dp[price_num]=dp[price_num]+dp[price_num-a*k] #새로운 가지수를 price_num에 갱신시키는 방법
        
print(dp[price])




    
#print(prices)
#print(arr[1][1])
