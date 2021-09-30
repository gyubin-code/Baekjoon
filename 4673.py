max_num =10000
find_num =[0 ]*(max_num+1)
for i in range(1,max_num+1):
    atmp =0
    k =i
    while i>0:
        atmp +=i%10
        i//=10

    tmp = k+atmp
   
    if(tmp >=10000):
        tmp =0
    find_num[tmp]=1 # 1이면 생성자가 있다는 것이다.


for i in range(9903,max_num):
    if(find_num[i]==0):
        print(i)


    
