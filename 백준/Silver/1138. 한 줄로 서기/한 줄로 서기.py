n = int(input())

pp = list(map(int,input().split()))
res = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == pp[i] and res[j] == 0:
            res[j] = i+1
            break
        elif res[j] == 0:
            cnt+=1

print(' '.join(map(str,res)))