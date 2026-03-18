n = int(input())
p = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = sum(a) - sum(b)
c = [p[i] - a[i] for i in range(n)]
c.sort()
ans += c[-1]
print(ans)
