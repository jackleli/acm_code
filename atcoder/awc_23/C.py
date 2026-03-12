n, m = map(int, input().split())
t = [0] + list(map(int, input().split()))
for i in range(n + 1):
  t[i] += t[i - 1]
for i in range(m):
  s, l, r = map(int, input().split())
  print(s + t[r] - t[l - 1])