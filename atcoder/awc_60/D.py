n = int(input())
p = []; q = []
for i in range(n):
  pi, qi = map(int, input().split())
  p.append(pi); q.append(qi)
ans = -1
for i in range(1 << n):
  ct = i.bit_count()
  if ct < 2:
    continue
  mulp, mulq = 1, 1
  for j in range(n):
    if i >> j & 1:
      mulp *= p[j]; mulq *= q[j]
  if mulp == mulq:
    if ans == -1 or ans > ct:
      ans = ct
print(ans)