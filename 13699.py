n=int(input())

dp=[0]*36
dp[0]=1

for i in range(1,36):
        # if(i%2==0):
        #         for k in range(int(i/2)):
        #                 dp[i]+=dp[k]+dp[i-1-k]*2
        # else:
        #         for k in range(int(i/2)+1):
        #                 dp[i]+=dp[k]+dp[i-1-k]*2
        #                 if(k==i-k-1):
        #                         dp[i]
        for k in range(i):
                #print(k,i-k-1)
                dp[i]+=dp[k]*dp[i-1-k]
                
        #print("dp[",i,"]=",dp[i])        
print(dp[n])