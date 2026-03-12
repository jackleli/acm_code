import copy
n, s, t = map(int, input().split())
dp = [[-10**9 for i in range(n + 1)] for i in range(s + 1)]
dp[0][0] = 0
for i in range(n):
  p, c, w = map(int, input().split())
  for j in range(s, w - 1, -1):
    for k in range(n, -1, -1):
      dp[j][k] = max(dp[j][k], dp[j - w][k - 1] + p - c)
ans = -1
for i in range(n, -1, -1):
  for j in range(0, s + 1):
    if dp[j][i] >= t:
      ans = i
print(ans)