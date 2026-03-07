N, M, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
l, r = 0, min(N, M)
def check(k):
  for i in range(0, k):
    if B[i] > A[N - k + i]:
      return False
  return True
while l < r:
  mid = (l + r + 1) >> 1
  if check(mid):
    l = mid
  else:
    r = mid - 1
print(l * C)
