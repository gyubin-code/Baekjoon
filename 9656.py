n = int (input())

m = int(n/3)

if( m%2==1):
    if(n%2==0):
        print("SK")
    else:
        print("CY")
else:
    if(n%2==1):
        print("CY")
    else:
        print("SK")
    