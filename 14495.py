n = int(input())
real_n = n-1
fn =[1,1,1]
for i in range(0,n-1):
    fn.append(fn[i]+fn[i+2])
print(fn)
print(fn[real_n])

