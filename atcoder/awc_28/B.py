n, l, r = map(int, input().split())
t = list(map(int, input().split()))
ans, cur = 0, 0
for i in range(n):
  if t[i] >= l and t[i] <= r:
    cur += 1
  else:
    ans = max(ans, cur)
    cur = 0
ans = max(ans, cur)
print(ans)