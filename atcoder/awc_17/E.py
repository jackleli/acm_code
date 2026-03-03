n = int(input())
point = [list(map(int, input().split())) for i in range(n)]
inf = 10**9
dp = [[inf for i in range(n)] for i in range(1 << n)]
dp[1][0] = 0

def dist(i, j):
  return (point[i][0] - point[j][0])**2 + (point[i][1] - point[j][1])**2

for mask in range(1, 1 << n):
  for i in range(n):
    if dp[mask][i] == inf:
      continue
    for j in range(n):
      if not mask >> j & 1:
        dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + dist(i, j))

ans = inf
for i in range(1, n):
  ans = min(ans, dp[(1 << n) - 1][i] + dist(i, 0))
print(ans)