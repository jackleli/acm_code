n, m, k = map(int, input().split())
t = list(map(int, input().split()))
arr = []
for i in range(1, n + 1):
  s = list(map(int, input().split()))
  ok = True
  for j in range(1, m + 1):
    if s[j - 1] < t[j - 1]:
      ok = False
      break
  if ok:
    arr.append((sum(s), i))
arr.sort(key=lambda x: -x[0])
ans = []
for s, idx in arr:
  if len(arr) <= k or s >= arr[k - 1][0]:
    ans.append(idx)
ans.sort()
print(*ans, sep='\n')