n, k = map(int, input().split())
ans = 0
for i in range(n):
  c, d = map(int, input().split())
  if c <= k:
    ans += d
print(ans)