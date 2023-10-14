import sys

input = sys.stdin.readline

n,m = map(int,input().split())

r,c,d = map(int,input().split())
# 0 - 북
# 1 - 동
# 2 - 남
# 3 - 서
room = []
for _ in range(n):
    room.append(list(map(int,input().split())))
visited = [[0] * m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 북동남서

visited[r][c] = 1
res = 1

while True:
    cnt = 0

    #4방향 확인
    for _ in range(4):
        nx = r + dx[(d+3)%4]
        ny = c + dy[(d+3)%4]
        d = (d+3) % 4

        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                res += 1
                r = nx
                c = ny
                cnt = 1
                break
    if cnt == 0:
        if room[r-dx[d]][c-dy[d]] == 1:
            print(res)
            break
        else:
            r = r-dx[d]
            c = c-dy[d]