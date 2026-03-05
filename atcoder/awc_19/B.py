n, k = map(int, input().split())
ans = 0
for i in range(n):
  s = input()
  if s.count('!') >= k:
    ans += 1
print(ans)