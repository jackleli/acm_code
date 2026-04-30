import sys
sys.setrecursionlimit(1000000)

n, q = map(int, input().split())
g = [[] for i in range(n + 1)]
p = list(map(int, input().split()))
for i in range(n - 1):
  g[p[i]].append(i + 2)
M = n.bit_length()
f = [[0 for i in range(M)] for i in range(n + 1)]
dep = [0] * (n + 1)

def dfs(u, fa):
  dep[u] = dep[fa] + 1
  f[u][0] = fa
  for j in range(1, M):
    f[u][j] = f[f[u][j - 1]][j - 1]
  for v in g[u]:
    if v == fa:
      continue
    dfs(v, u)

dfs(1, 0)

def lca(u, v):
  if dep[u] < dep[v]:
    u, v = v, u
  for i in range(M - 1, -1, -1):
    if dep[f[u][i]] >= dep[v]:
      u = f[u][i]
  if u == v:
    return u
  for i in range(M - 1, -1, -1):
    if f[u][i] != f[v][i]:
      u = f[u][i]
      v = f[v][i]
  return f[u][0]

for i in range(q):
  x, y = map(int, input().split())
  print(lca(x, y))
