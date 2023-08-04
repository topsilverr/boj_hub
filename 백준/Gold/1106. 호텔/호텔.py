import sys

input = sys.stdin.readline

c,n = map(int,input().split())
max_cost = float('INF')
price = [[0,0]]
for i in range(n):
    price.append(list(map(int,input().split())))

dp = [[max_cost for _ in range(c+1)] for _ in range(n+1)]
# dp[i][j] : i번째 도시까지 선택해서 적어도 j 이득을 보기 위한 최소 비용

for i in range(1,n+1): # 도시
    ben = price[i][1] # 1명일 때 이득
    cost = price[i][0] # 0명일 때 이득 = 02

    for j in range(1,c+1):
        dp[i][j] = dp[i-1][j]

        k = 0 # 이 도시에서 몇명을 늘릴건지 -> 한 도시에서 여러 명 늘릴 수도 있으니까 따로 변수 설정 해줌
        while True:
            if j - (k*ben) <= 0:
                dp[i][j] = min(dp[i][j],k*cost)
                break
            else:
                dp[i][j] = min(dp[i][j],dp[i-1][j-k*ben]+k*cost)

            k+=1
print(dp[n][-1])