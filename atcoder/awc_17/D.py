n, m, k = map(int, input().split())
a = list(map(int, input().split()))
edge = [] * m
for i in range(m):
  edge.append(list(map(int, input().split())))
ans = -10**18
for mask in range(1 << n):
  if mask.bit_count() != k:
    continue
  res = sum(a[i] for i in range(n) if mask >> i & 1)
  for u, v, w in edge:
    u -= 1
    v -= 1
    if (mask >> u & 1) and (mask >> v & 1):
      res -= w
  ans = max(ans, res)
print(ans)