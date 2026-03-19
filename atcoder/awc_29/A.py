n, p, b, k = map(int, input().split())
c = list(map(int, input().split()))
ans = 0
for i in range(n):
  ans += (p + b) * c[i] if c[i] >= k else p * c[i]
print(ans)