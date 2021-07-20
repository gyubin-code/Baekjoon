n,k = map(int,input().split())

arr =[] #계란판
add_arr=[]
flag =[]*n

for i in range(n):
    arr.append(list(map(int,input().split())))


for i in range(n-1):
    for j in range(n-1):
        add_arr.append(arr[i][j]+arr[i][j+1])
        add_arr.append(arr[i][j]+arr[i+1][j])

print(add_arr)

new_n =n-1
rkfla = [] #가림막 위치 저장




