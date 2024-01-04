n = int(input())
st = [0] * 301
for s in range(1,n+1):
    st[s] = int(input())

dp = [0] * 301 # n번째 계단에서의 최댓값

dp[1] = st[1]
dp[2] = st[1] + st[2]
dp[3] = max(st[1]+st[3],st[2]+st[3])

for i in range(4,n+1):
    dp[i] = max(st[i]+st[i-1]+dp[i-3], st[i]+dp[i-2])

print(dp[n])