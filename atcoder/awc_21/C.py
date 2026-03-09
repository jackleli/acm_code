N, K = map(int, input().split())
vec = []
for i in range(N):
  input_data = list(map(int, input().split()))
  C, M = input_data[0], input_data[1]
  P = input_data[2:]
  tot = sum(P) - C
  if tot > 0:
    vec.append(tot)
vec.sort(reverse=True)
ans = 0
for i in range(min(K, len(vec))):
  ans += vec[i]
print(ans)