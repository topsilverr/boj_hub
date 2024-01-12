# 토마토가 있는 곳 죄표 저장
# 그 좌표 돌면서 익히면 1로 바꿈 그래서 각 좌표마다 얼마나 걸리는지 계산
# 시간 중 최대 시간 출력

# m이 가로 즉 x n이 세로 즉 y

from collections import deque
n,m = map(int,input().split())
tomato = []
isTom = deque()
for i in range(m):
    tomato.append(list(map(int,input().split())))

# 익은 토마토가 있는 좌표 저장
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            isTom.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs():
    while isTom:
        x,y = isTom.popleft()
        for p in range(4):
            nx = x+dx[p]
            ny = y+dy[p]
            if nx >= m or ny >= n or nx < 0 or ny < 0:
                continue
            elif tomato[nx][ny] != 0:
                continue
            else:
                tomato[nx][ny] = tomato[x][y] + 1
                isTom.append((nx,ny))

bfs()
ans = 0
for line in tomato:
    for t in line:
        if t == 0:
            print(-1)
            exit(0)
    ans = max(ans,max(line))
print(ans-1)