a = int(input())
dp = [0]*a
dp[0] = 1
if a <= 1:
    print(1)
    exit()
dp[1] = 1
for i in range(2,a):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[a-1])
