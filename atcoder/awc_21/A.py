N, K = map(int, input().split())
ans = 0
for i in range(N):
  v = list(map(int, input().split()))
  sz = v[0]
  ans += sum(1 for i in range(1, sz + 1) if v[i] >= K)
print(ans)