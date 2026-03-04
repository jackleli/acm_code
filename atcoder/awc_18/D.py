import copy
n, k = map(int, input().split())
c = list(map(int, input().split()))
dp = [0] * (k + 1)
for i in range(n):
  ndp = copy.deepcopy(dp)
  for j in range(k + 1):
    if j + c[i] <= k:
      ndp[j + c[i]] = max(ndp[j + c[i]], dp[j] + c[i])
  dp = ndp
print(dp[k])