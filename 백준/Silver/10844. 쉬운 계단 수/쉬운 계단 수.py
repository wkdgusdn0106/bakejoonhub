a = int(input())
mod = 10**9
dp = [[0]*10 for i in range(a+1)]
for i in range(1,10):
    dp[1][i] = 1
for i in range(2,a+1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i-1][j-1]%mod
        if j < 9:
            dp[i][j] += dp[i-1][j+1]%mod
print(sum(dp[-1])%mod)
