n, m, t = map(int, input().split())
dp = [0] * (m + 1)
for i in range(n):
  a, b, c = map(int, input().split())
  ndp = [0] * (m + 1)
  for j in range(m + 1):
    ndp[j] = max(ndp[j], dp[j] + (b >= t) * a)
    if j + c <= m:
      ndp[j + c] = max(ndp[j + c], dp[j] + a)
  dp = ndp
print(dp[m])