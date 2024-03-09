from collections import deque
import sys

input = sys.stdin.readline

que = deque()

n = int(input())

for _ in range(n):
    cmd = input().strip()

    if "push" in cmd:
        c,n = cmd.split()
        que.append(n)
    elif cmd == "pop":
        if que:
            print(que.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif cmd == "top":
        if que:
            print(que[len(que)-1])
        else:
            print(-1)