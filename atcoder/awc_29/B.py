n, q = map(int, input().split())
v = [0] + list(map(int, input().split()))
for i in range(q):
  opt = list(map(int, input().split()))
  if opt[0] == 1:
    v[opt[1]], v[opt[2]] = 0, v[opt[1]] + v[opt[2]]
  else:
    print(v[opt[1]])
