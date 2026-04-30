n, m = map(int, input().split())
a = list(map(int, input().split()))
c = [0] * (n + 1)
for i in range(m):
  l, r = map(int, input().split())
  c[l] += 1
  if r < n:
    c[r + 1] -= 1
ans = []
for i in range(1, n + 1):
  c[i] += c[i - 1]
  ans.append(c[i] * a[i - 1])
print(*ans, sep=" ")