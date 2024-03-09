import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    ps = input().strip()

    open = 0

    for p in ps:

        if p == ")" and open > 0:
            open-=1
        elif p == ")" and open <= 0:
            open = -2
            break
        if p == "(":
            open+=1

    if open == 0:
        print("YES")
    else:
        print("NO")