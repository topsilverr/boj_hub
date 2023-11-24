# 조합을 통해서 벽을 세울 수 있는 경우의 수 구하고 for문,,,돌리면서 안전구역 개수 구하기
from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 빈 칸 좌표 리스트 만들어서 벽 세울 칸 조합 구하기
empty_list = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            empty_list.append((x, y))
wall_case = list(combinations(empty_list, 3))


# 바이러스 퍼짐
def bfs(i, j, virusGraph):
    que = deque()
    que.append((i, j))

    while que:
        x, y = que.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if virusGraph[nx][ny] == 0:
                virusGraph[nx][ny] = 2
                que.append((nx, ny))


result = []
for three_wall in wall_case:
    virusGraph = copy.deepcopy(graph)  # 벽이 세워질 칸 케이스 별로 그래프 생성하기 위해 deepcopy
    # 벽 세개 만들기
    for wall in three_wall:
        wall_x, wall_y = wall
        virusGraph[wall_x][wall_y] = 1  # 벽을 세움

    for i in range(n):
        for j in range(m):
            if virusGraph[i][j] == 2:  # 2인 곳에서 바이러스 퍼져나가니까 2인 곳에서 바이러스 전파
                bfs(i, j, virusGraph)

    cnt = 0
    for p in range(n):
        for q in range(m):
            if virusGraph[p][q] == 0:
                cnt += 1
    result.append(cnt)
    # 바이러스가 가장 적게 퍼진수를 저장하기

print(max(result))