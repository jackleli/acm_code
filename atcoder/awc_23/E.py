n, c = map(int, input().split())
w = list(map(int, input().split()))
inf = 10**9
dp = [inf] * (1 << n)
cost = [0] * (1 << n)

for i in range(1 << n):
  for j in range(n):
    if i >> j & 1:
      cost[i] += w[j]

dp[0] = 0
for i in range(1 << n):
  j = i
  while j < 1 << n:
    k = i ^ j
    if cost[k] <= c:
      dp[j] = min(dp[j], dp[i] + 1)
      # print(j, i, dp[i], dp[j], k, cost[k])
    j = i | (j + 1)

print(dp[(1 << n) - 1])
