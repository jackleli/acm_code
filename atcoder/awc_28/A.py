n, k = map(int, input().split())
p = list(map(int, input().split()))
print(sum(v for v in p if v >= k))