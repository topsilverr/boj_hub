n = int(input())
arr = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

max_val = -int(1e9)
min_val = int(1e9)

def dfs(i,data):
    global max_val,min_val,add,sub,mul,div

    if i == n:
        max_val = max(max_val,data)
        min_val = min(min_val,data)
    else:
        if add > 0:
            add-=1
            dfs(i+1,data + arr[i])
            add += 1
        if sub > 0:
            sub-=1
            dfs(i+1,data-arr[i])
            sub+=1
        if mul > 0:
            mul-=1
            dfs(i+1,data*arr[i])
            mul+=1
        if div > 0:
            div-=1
            dfs(i+1,int(data/arr[i]))
            div+=1

dfs(1,arr[0])

print(max_val)
print(min_val)