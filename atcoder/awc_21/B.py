N, M = map(int, input().split())
P = [0] + list(map(int, input().split()))
for i in range(N):
  v = list(map(int, input().split()))
  idx = 0
  for i in range(1, v[0] + 1):
    if P[v[i]] > P[idx]:
      idx = v[i]
    elif P[v[i]] == P[idx]:
      idx = min(idx, v[i])
  print(idx)