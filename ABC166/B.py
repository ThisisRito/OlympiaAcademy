N, K = list(map(int, input().split()))
cnt = {i: 0 for i in range(1, N+1)}
for _ in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        cnt[a] += 1
res = len([k for k, v in cnt.items() if v == 0])
print(res)