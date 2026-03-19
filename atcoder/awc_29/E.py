n, m = map(int, input().split())
INF = 10**18
d = [[0 if i == j else INF for j in range(n)] for i in range(n)]
for i in range(m):
  u, v, w = map(int, input().split())
  u -= 1; v -= 1
  d[u][v] = min(d[u][v], w)
for k in range(n):
  for i in range(n):
    for j in range(n):
      d[i][j] = min(d[i][j], d[i][k] + d[k][j])
s, k = map(int, input().split())
s -= 1
t = list(map(int, input().split()))
dp = [[INF for i in range(k)] for i in range(1 << k)]
for i in range(k):
  t[i] -= 1
  dp[1 << i][i] = d[s][t[i]]
for i in range(1 << k):
  for j in range(k):
    if dp[i][j] == INF:
      continue
    for x in range(k):
      if not i >> x & 1:
        dp[i | (1 << x)][x] = min(dp[i | (1 << x)][x], dp[i][j] + d[t[j]][t[x]])
ans = INF
for i in range(k):
  ans = min(ans, dp[(1 << k) - 1][i] + d[t[i]][s])
print(-1 if ans == INF else ans)