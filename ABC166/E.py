from collections import defaultdict
N = map(int, input().split())
A = list(map(int, input().split()))
res = 0
d = defaultdict(int)
for i, num in enumerate(A):
    res += d[i - num]
    d[i + num] += 1
print(res)