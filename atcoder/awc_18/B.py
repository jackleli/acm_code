n, m = map(int, input().split())
c = list(map(int, input().split()))
tot = [0] * m
ans = 0
for i in range(n):
  k = int(input())
  p = list(map(int, input().split()))
  for j in range(k):
    tot[p[j] - 1] += 1
  for j in range(k):
    if tot[p[j] - 1] <= c[p[j] - 1]:
      ans += 1
  for j in range(k):
    tot[p[j] - 1] -= 1
print(ans)