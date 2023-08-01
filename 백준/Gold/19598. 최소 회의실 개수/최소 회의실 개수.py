import sys, heapq

input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

endTime = []
nums.sort()

heapq.heappush(endTime, nums[0][1])

res = 1
for i in range(1, n):
    if nums[i][0] < endTime[0]:
        res += 1
        heapq.heappush(endTime, nums[i][1])
    else:
        heapq.heappop(endTime)
        heapq.heappush(endTime, nums[i][1])

print(res)