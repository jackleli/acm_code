n, k = map(int, input().split())
a = list(map(int, input().split()))
p = list(map(int, input().split()))
MOD = 10**9 + 7

# 方法一: dp[i][j]: 表示考虑了p序列的前i个, 当且在a选择的子序列末尾是j的方案数
# dp = [0] * n
# for i in range(n):
#   if a[i] == p[0]:
#     dp[i] = 1
# for i in range(1, k):
#   pre = 0
#   ndp = [0] * n
#   for j in range(n):
#     if a[j] == p[i]:
#       ndp[j] = (ndp[j] + pre) % MOD
#     pre = (pre + dp[j]) % MOD
#   dp = ndp
# ans = 0
# for i in range(n):
#   ans = (ans + dp[i]) % MOD
# print(ans)

# 方法二: dp[i][j]: 表示考虑了a序列的前i个，与p序列的前j个形成子序列的方案数
# dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] (如果a[i] == )
# 考虑滚动数组, 倒叙更新j即可

dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
  for j in range(k, 0, -1):
    if a[i] == p[j - 1]:
      dp[j] = (dp[j] + dp[j - 1]) % MOD

print(dp[k])