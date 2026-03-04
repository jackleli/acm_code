# 法1: O(N^3)

# n, k, b = map(int, input().split())
# cs = [list(map(int, input().split())) for i in range(n)]
# dp = [[-10**9 for i in range(b + 1)] for i in range(n)]
# ans = 0
# for i in range(n):
#   c, s = cs[i]
#   if c <= b:
#     dp[i][c] = 1
#   for j in range(b + 1):
#     for z in range(0, i):
#       if cs[z][1] < s and j + c <= b:
#         dp[i][j + c] = max(dp[i][j + c], dp[z][j] + 1)
#   for j in range(b + 1):
#     ans = max(ans, min(dp[i][j], k))
# print(ans)

# 法2: O(K * N * logN)
n, k, b = map(int, input().split())
cs = [list(map(int, input().split())) for i in range(n)]
vec = sorted(list(set([s for c, s in cs])))  
value_to_index = {num: idx + 1 for idx, num in enumerate(vec)}
id_vec = [value_to_index[s] for c, s in cs]
dp = [c for c, s in cs]
ans = 0
for i in range(n):
  if dp[i] <= b:
    ans = 1
vec_sz = len(vec)
for _ in range(2, k + 1):
  ndp = [10**9] * n
  bit = [10**9] * (vec_sz + 1)
  def ask(x):
    res = 10**9
    while x > 0:
      res = min(res, bit[x])
      x -= x & -x
    return res
  def update(x, v):
    while x <= vec_sz:
      bit[x] = min(bit[x], v)
      x += x & -x
  for i in range(n):
    idx = id_vec[i]
    ndp[i] = min(ndp[i], ask(idx - 1) + cs[i][0])
    update(idx, dp[i])
    if ndp[i] <= b:
      ans = _
  dp = ndp
print(ans)