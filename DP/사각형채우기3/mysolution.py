n=int(input())

dp=[0]*(n+1)

dp[0]=1
dp[1]=2

for i in range(2,n+1):
    dp[i]=(2 * dp[i-1] + 3 * dp[i-2]) % 1000000007
    for j in range(i-3,-1,-1): #i-3~ 0까지 항상 2개씩 존재
        dp[i]=(dp[i]+ 2*dp[j]) % 1000000007

print(dp[n])
