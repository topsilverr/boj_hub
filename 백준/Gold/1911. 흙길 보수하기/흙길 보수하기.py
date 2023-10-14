import sys

input = sys.stdin.readline

n,l = map(int,input().split())

pool = []
for _ in range(n):
    pool.append(list(map(int,input().split())))

pool.sort(key=lambda x:x[0])

chk = 0
point = pool[0][0]

res = 0
for s,e in pool:
    if point > e :
        continue
    elif point < s:
        point = s

    dist = e - point
    re = 1
    if dist % l == 0:
        re = 0
    count = (dist // l) + re

    point += count * l
    res += count

print(res)