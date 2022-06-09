import sys

lambda input: sys.stdin.readline().rstrip

def multi(a, n):
    if n == 1:
        return a % c
    else:
        tmp = multi(a, n//2)
        if n % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

if __name__ == '__main__':
    a, b, c = map(int, input().split())

    # 지수 나머지 분배 법칙을 알야야함
    # (AxB)%C = (A%C) *(B%C) % C

    print(multi(a, b))


