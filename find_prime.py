import sys

read= sys.stdin.readline
prime_num=[]
queue=[]

N=int(input())

a= list(map(int,read().split())) #리스트로 변환시켜야함


def find_prime(a,N):
    # # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)//전체를 소수로 가ㄴ주
    # sieve = [True] * N

    # # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    # m = int(N ** 0.5)
    # for i in range(2, m + 1):
    #     if sieve[i] == True:           # i가 소수인 경우
    #         for j in range(i+i, N, i): # i이후 i의 배수들을 False 판정
    #             sieve[j] = False

    # # 소수 목록 산출
    # return [i for i in range(2, N) if sieve[i] == True]
    cnt=0
    a=sorted(a)  # 정렬
    max_num= a[N-1] #7이 빠져나옴
    #print(max_num)

    sieve=[True]*(max_num+1)
    sieve[1]=False #1은 소수가 아님

    #검사할 부분 찾기 루트 제일 큰것까지 판별한다

    rut=int(max_num**(1/2))
    # 범위가 i가 2부터 rut+1까지
    for i in range(2,rut+1):
        if sieve[i]==True:
            for j in range(i+i,max_num+1,i):# i를 제외한 max num까지 리스트,, 
                sieve[j]=False
    print(sieve)
    for k in a:
        if sieve[k]==True:
            cnt+=1
            #print(k)
    return print(cnt)

   


find_prime(a,N)




