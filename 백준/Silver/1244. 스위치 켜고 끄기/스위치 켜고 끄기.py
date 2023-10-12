n = int(input())

light = list(map(int,input().split()))

s = int(input())

for _ in range(s):
    s, a = map(int,input().split())
    i = 1
    if s == 1:
        while i*a <= n:
            buf = i * a
            if light[buf - 1] == 0:
                light[buf - 1] = 1
            else:
                light[buf - 1] = 0
            i += 1
            if buf > n:
                break
    else:
        if light[a-1] == 0:
            light[a - 1] = 1
        else:
            light[a - 1] = 0
        while a - i - 1 >= 0 and a + i - 1 < n:
            if light[a - i - 1] == light[a + i - 1] == 0:
                light[a - i - 1] = 1
                light[a + i - 1] = 1
            elif light[a - i - 1] == light[a + i - 1] == 1:
                light[a - i - 1] = 0
                light[a + i - 1] = 0
            else:
                break
            i += 1
            if a - i - 1 < 0 or a + i - 1 >= n:
                break

for i in range(n):
    print(light[i], end = " ")
    if i % 20 == 19 :
        print()
