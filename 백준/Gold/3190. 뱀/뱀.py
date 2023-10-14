import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [([0] * n) for _ in range(n)]

k = int(input())
apples = []
for _ in range(k):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    board[a][b] = 1
    apples.append((a,b))

l = int(input())
move = []
for i in range(l):
    move.append(list(input().split()))
    move[i][0] = int(move[i][0])

time = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

nd,x,y = 0,0,0 # n 은 초기방향
i=0
snake = deque()
snake.append((0,0))

while True:
    time += 1
    x = x + dx[nd]
    y = y + dy[nd]
    if x < 0 or x >= n or y < 0 or y >= n or (x,y) in snake:
        break
    snake.append((x,y))
    if board[x][y] == 0:
        snake.popleft() # 원래 꼬리 있었던 위치 pop
    else:
        board[x][y] = 0
    if time == move[i][0]:
        if move[i][1] == 'L':
            nd = (nd-1) % 4
        else:
            nd = (nd+1) % 4
        if i + 1 < len(move):
            i += 1

print(time)