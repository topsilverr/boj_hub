import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())

ctr = []
for i in range(n):
    ctr.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(i, j):
    que = deque()
    check = []
    que.append((i, j))
    check.append((i, j))
    while que:
        x, y = que.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            elif l <= abs(ctr[x][y] - ctr[nx][ny]) <= r and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                que.append((nx, ny))
                check.append((nx, ny))

    return check


# dfs로 구역 나눠서 열린 곳 list에 좌표 저장
# visited 만들어서 visited 아닌 곳만 다시 dfs 호출
# 구역 나눠서 구역별로 계산하고

cnt = 0
while True:
    visited = [[0] * n for _ in range(n)]
    chk = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                res_u = bfs(i, j)

                if len(res_u) > 1:
                    chk = 1
                    move = sum(ctr[x][y] for x, y in res_u) // len(res_u)

                    for x, y in res_u:
                        ctr[x][y] = move
    if chk == 0:
        print(cnt)
        break

    cnt += 1