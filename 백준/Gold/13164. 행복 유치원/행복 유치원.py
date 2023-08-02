import sys

input = sys.stdin.readline

n,k = map(int,input().split())

kids = list(map(int,input().split()))

chk = []

for i in range(n-1):
    chk.append(kids[i+1] - kids[i])

chk.sort()
res = 0
for i in range(n-k):
    res += chk[i]
print(res)