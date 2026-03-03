n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(m):
  p = b[i] - 1
  a[p] += 1
  if p - 1 >= 0:
    a[p - 1] += 1
  if p + 1 < n:
    a[p + 1] += 1
print(*a, sep=" ")