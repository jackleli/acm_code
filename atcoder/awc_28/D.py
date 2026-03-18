import heapq

n, m = map(int, input().split())
g = [[] for i in range(n + 1)]
rd = [0] * (n + 1)
for i in range(m):
  u, v = map(int, input().split())
  g[u].append(v)
  rd[v] += 1

pq = []

for i in range(1, n + 1):
  if rd[i] == 0:
    heapq.heappush(pq, i)

ans = []

while len(pq) > 0:
  u = heapq.heappop(pq)
  ans.append(u)
  for v in g[u]:
    rd[v] -= 1
    if rd[v] == 0:
      heapq.heappush(pq, v)

print(*ans, sep=" ")