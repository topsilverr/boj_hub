import math
t = int(input())

for i in range(t):
    n,m = map(int,input().split())
    res = math.comb(m,n)
    print(res)