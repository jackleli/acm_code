from collections import defaultdict
N = int(input())
mp = defaultdict(lambda: defaultdict(int))
for i in range(N):
  P, Q = map(int, input().split())
  mp[P][Q] += 1
ans = 0
for k, vmp in mp.items():
  pre = 0
  for s, t in vmp.items():
    ans += pre * t
    pre += t
print(ans)