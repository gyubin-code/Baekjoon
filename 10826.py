n = int(input())
fn =[0]*10001
fn[1]=1
for i in range(2,10001):
    fn[i]=fn[i-1]+fn[i-2]

print(fn[n])

