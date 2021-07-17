arr =[]
for i in range(10):
    n=int(input())
    arr.append(n%42)

arr= set(arr)#중복제거 필터
print(len(arr))   
