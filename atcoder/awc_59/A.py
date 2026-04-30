n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(0, n - 1):
  if a[i] != -1 and a[i + 1] != -1:
    if a[i] > a[i + 1]:
      ans += 1
      a[i] += a[i + 1] // 2
      a[i + 1] = -1
    elif a[i] < a[i + 1]:
      ans += 1
      a[i + 1] += a[i] // 2
      a[i] = -1
print(n - ans)