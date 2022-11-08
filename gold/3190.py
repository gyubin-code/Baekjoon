max_num =10000
find_num =[0 ]*(max_num+1)
for i in range(1,max_num):
    #i는 숫자
    a=0
    b=0
    c=0
    d=0
    if i>=0:
        one = i
        if(i>=10):
            a= int(i/10)
            one = i%10
            if(i>=100):
                b = int(i/100)
                one = i%100
                if(i>=1000):
                    c = int(i/1000)
                    one = i%1000
   
    
    tmp = i+a+b+c+one
    if(tmp >=10000):
        tmp =0
    find_num[tmp]=1 # 1이면 생성자가 있다는 것이다.


for i in range(max_num):
    if(find_num[i]==0):
        print(i)


    
