n = int(input())
dp = [0]*100
dp[0] = 1
dp[1] = 2
idx = 0
for i in range(2,100):
    dp[i] = dp[i-1] + dp[i-2]
    if dp[i] >= n:
        idx = i
        break
if n in dp:
    print(-1)
else:
    for i in range(idx,-1,-1):
        if dp[i] == n:
            print(dp[i])
            break
        if dp[i] < n:
            n-=dp[i]
