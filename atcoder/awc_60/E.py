n, q, m = map(int, input().split())
d = []
p = []
for i in range(n):
  di, pi = map(int, input().split())
  pi -= 1
  d.append(di)
  p.append(pi)
MAX_LOG = 60
f = [[0 for i in range(MAX_LOG)] for i in range(n)]
g = [[0 for i in range(MAX_LOG)] for i in range(n)]
pw10 = [0] * MAX_LOG
pw10[0] = 10 % m
for j in range(0, MAX_LOG):
  if j > 0:
    pw10[j] = pw10[j - 1] * pw10[j - 1] % m
  for i in range(n):
    if j == 0:
      g[i][j] = p[i]; f[i][j] = d[i]
    else:
      g[i][j] = g[g[i][j - 1]][j - 1]
      f[i][j] = (f[i][j - 1] * pw10[j - 1] % m + f[g[i][j - 1]][j - 1]) % m
# for i in range(n):
#   for j in range(MAX_LOG):
#     print(f"f[{i}][{j}] = {f[i][j]}")
for i in range(q):
  s, k = map(int, input().split())
  s -= 1
  v = 0
  for i in range(0, MAX_LOG):
    if k >> i & 1:
      v = (v * pw10[i] % m + f[s][i]) % m
      s = g[s][i]
  print(v)