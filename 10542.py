import sys
#필요한 자료형
arr =[0]
read=sys.stdin.readline

#input 먼저 적기
n= int(read())
num_people =[0]*(n+1) # 각 인데
for i in range(n):
    arr.append(int(read())) #arr =[2,1,1]
#내가 생각한 조건

#내가 간과한것, 마피아끼리는 서로 가리키지 않는다
# 즉 a[i]=a, arr[a]=i 인 경우에는, 해당되지않는다
# 걍 잘 모르겠고 잎의 갯수인거같다.



