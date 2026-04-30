from collections import defaultdict
n = int(input())
s = input()
mp = defaultdict(int)
cur, ans = 0, 0
mp[cur] += 1
for c in s:
  if c == 'V':
    cur += 1
  elif c == 'F':
    cur -= 1
  ans += mp[cur]
  mp[cur] += 1
print(ans)
