import heapq
N, M, K = map(int, input().split())
g = [[] for i in range(N)]
for i in range(M):
  U, V, T = map(int, input().split())
  U -= 1; V -= 1
  g[U].append((V, T))
  g[V].append((U, T))
P = [1] + list(map(int, input().split())) + [N]
sz = len(P)
inf = 10**18
d = [[inf for i in range(N)] for i in range(sz)]
def dijkstra(st, dis):
  dis[st] = 0
  pq = []
  vis = [False for i in range(N)]
  heapq.heappush(pq, (0, st))
  while len(pq) > 0:
    dep, u = heapq.heappop(pq)
    if vis[u]:
      continue
    vis[u] = True
    for v, t in g[u]:
      if dis[v] > dis[u] + t:
        dis[v] = dis[u] + t
        heapq.heappush(pq, (dis[v], v))

for i in range(sz):
  P[i] -= 1
  dijkstra(P[i], d[i])

ans = 0
for i in range(1, sz):
  if d[i - 1][P[i]] == inf:
    ans = -1
    break
  else:
    ans += d[i - 1][P[i]]
print(ans)
