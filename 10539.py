
n = int(input())
b= list(map(int,input().split()))
a_list=[]
a_list.append(b[0])
for i in range(1,n):
    a_list.append(b[i]*(i+1)-sum(a_list))
for i in a_list:
    print(i,end=' ')


