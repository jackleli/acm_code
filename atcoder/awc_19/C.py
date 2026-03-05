n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
i = 0
while i < n:
  j = i + 1
  while j < n and a[j] == a[j - 1] + 1:
    j += 1
  ans += 1
  i = j
print(ans)