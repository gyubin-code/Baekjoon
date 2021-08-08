n = int(input())

def nCr(n,r):
    num = 1;
    deno=1;
    r = min(n-r,r)
    for i in range(1,r+1):
        deno *=i
        num *=n+1-i
    return num / deno

for _ in range(n):
    a,b = map(int,input().split())
    print(int(nCr(b,a)))
