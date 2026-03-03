n, q = map(int, input().split())
c = list(map(int, input().split()))
s = [0] * (n + 1)
for i in range(1, n):
  s[i] = s[i - 1] + (c[i] == c[i - 1])
for i in range(q):
  l, r = map(int, input().split())
  print(s[r - 1] - s[l - 1])