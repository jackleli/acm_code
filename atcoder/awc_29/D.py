from collections import deque

n, m, k = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
  u, v, w = map(int, input().split())
  u -= 1; v -= 1
  if w >= k:
    g[u].append(v)
    g[v].append(u)
d = [-1] * n
d[0] = 0
que = deque()
que.append(0)
while len(que) > 0:
  u = que.popleft()
  for v in g[u]:
    if d[v] == -1:
      d[v] = d[u] + 1
      que.append(v)
print(d[n - 1])
