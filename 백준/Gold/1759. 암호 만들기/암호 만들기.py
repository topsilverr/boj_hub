from itertools import combinations
l,c = map(int,input().split())

alp = list(map(str,input().split()))
alp.sort()

vowl = ['a','e','i','o','u']

comb = list(combinations(alp,l))

for li in comb:
    v = 0
    c = 0
    for p in li:
        if p in vowl:
            v+=1
        else:
            c+=1
    if v >= 1 and c>=2:
        print(''.join(li))