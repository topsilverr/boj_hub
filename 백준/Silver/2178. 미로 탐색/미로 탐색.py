from collections import deque
n,m = map(int,input().split())
graph= []
for i in range(n):
    graph.append(list(map(int,input())))

# 모든 경우의 수 확인 -> 최소 길 출력?

# 남북동서
dx = [1,-1,0,0]
dy = [0,0,1,-1]

#0,0 에서만 시작
def bfs(x,y):

    que = deque()
    que.append((x,y))

    while que:
        x,y = que.popleft()
        for p in range(4):
            nx = x+dx[p]
            ny = y+dy[p]
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            elif graph[nx][ny] == 1:
                que.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[n-1][m-1]

print(bfs(0,0))