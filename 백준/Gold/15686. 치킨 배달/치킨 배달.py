# r : 가로로 c : 세로로 -> 1번부터 시작
# 0 : 빈칸
# 1 : 집
# 2 : 치킨집
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 최대 m 개의 치킨 집을 조합으로 골라서 각 집별로 치킨 거리 구하고 도시 치킨거리 구해서 최소로 되는 거리 리턴

chic = []
# 치킨집 조합 구하기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chic.append((i, j))
comb = list(combinations(chic, m))

city = []
dis = 100

for chk in comb:
    buf = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                for p, q in chk:
                    dis = min(dis, abs(i - p) + abs(j - q))
                buf += dis
                dis = 100
    city.append(buf)

print(min(city))