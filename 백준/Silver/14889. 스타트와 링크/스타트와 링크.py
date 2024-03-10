import sys

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

chk = [False for _ in range(n)]

min_value = sys.maxsize

def backTracking(depth,idx):
    global min_value

    if depth == n//2:
        tp1,tp2 = 0,0

        for i in range(n):
            for j in range(n):
                if chk[i] and chk[j]:
                    tp1+=graph[i][j]
                elif not chk[i] and not chk[j]:
                    tp2+=graph[i][j]
        min_value = min(min_value,abs(tp1-tp2))

    for i in range(idx,n):
        if not chk[i]:
            chk[i] = True
            backTracking(depth+1,i+1)
            chk[i] = False

backTracking(0,0)
print(min_value)