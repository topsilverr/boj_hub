# 구역 구분 짓기 => bfs
from collections import deque
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

# 북동남서
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y,k):
    que = deque()
    que.append((x,y))
    visited[x][y] = 1

    while que:
        x,y = que.popleft()
        for p in range(4):
            nx = x + dx[p]
            ny = y + dy[p]

            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            elif arr[nx][ny] > k and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                que.append((nx,ny))

res = -1
for k in range(101):
    cnt = 0
    visited = [[0] * n for i in range(n)]  # 방문 확인
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and visited[i][j] == 0:
                bfs(i,j,k)
                cnt += 1
    if cnt==0:
        break
    res = max(res,cnt)

print(res)
