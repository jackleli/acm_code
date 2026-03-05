n, k = map(int, input().split())
s = list(map(int, input().split()))
print(sum(1 for sc in s if sc >= k))