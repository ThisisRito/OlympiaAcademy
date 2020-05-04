N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
e = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    e[a].append(b)
    e[b].append(a)

res = 0
for cur in range(1, N+1):
    isObser = True
    for u in e[cur]:
        if H[u-1] >= H[cur-1]:
            isObser = False
    res += int(isObser)
print(res)