n, k = map(int, input().split())
l = list(map(int, input().split()))
mx = max(l)
ans = sum(l) - mx
MOD = 10**9 + 7
res, a = mx, 2
while k > 0:
  if k & 1: 
    res = res * a % MOD
  a = a * a % MOD
  k >>= 1
print((ans + res) % MOD)