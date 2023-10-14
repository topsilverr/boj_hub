import sys,heapq

input = sys.stdin.readline

n = int(input())
cls = []
for _ in range(n):
    cls.append(list(map(int,input().split())))

res = 1

cls.sort()

# end = [0] * n
# end[1] = cls[0][1]
# 이거를 heapq 로?
end = []
heapq.heappush(end,cls[0][1])

for i in range(1,n):
    if end[0] > cls[i][0]:
        res+=1
        heapq.heappush(end,cls[i][1])
    else:
        heapq.heappop(end)
        heapq.heappush(end,cls[i][1])

print(res)