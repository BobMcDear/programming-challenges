n = int(input())
dp = [0]*(n+10)
s = [0]*(n+10)
chert = [0]*(n+10)
mod = 998244353 
pow10 = [1]*(n+10)
for i in range(1, n+1):
    pow10[i] = (pow10[i-1] * 10) % mod

"""
for i in range(n):
    dp[i] = f(i) - (dp[i-1]*2+dp[i-2]*3+...+dp[0]*(n))

dp[1] = 10
dp[2] = 180
dp[3] = 3000 - (dp[2]*2 + dp[1]*3) = 2610
dp[4] = 40000 - (dp[3]*2 + dp[2]*3 + dp[1]*4) = n*10**n - (s[n-1] + dp[n-1] + chert[n-1])

dp[n] = n*10**n - (s[n-1] + dp[n-1])
dp[n] = n*10**n - (dp[1]+dp[2]+...+dp[n-1]+dp[n-1])
dp[2]*2 + dp[1]*3
dp[3]*2 + dp[2]*3 + dp[1]*4 = dp[2]*2 + dp[1]*3 + (dp[3]*2 + dp[2] + dp[1] = s[3] + dp[3])
s[i] = dp[1]+dp[2]+...+dp[i]

dp[n] = 



"""
for i in range(1, n+1):
    p = (i *  pow10[i]) % mod
    dp[i] = (p - (s[i-1] + dp[i-1] + chert[i-1]))%mod
    s[i] = (dp[i]+s[i-1])%mod
    chert[i] = chert[i-1]+s[i-1]+dp[i-1]

"""print(pow10[:10])
print(dp[:10])
print(s[:10])
print(chert[:10])"""

for i in range(n, 0, -1):
    print(dp[i], end=' ')
print()