n, a, b = map(int, input().split())

inf = 10**18

def max_plus_mult(a, b):
  c = [[-inf for i in range(2)] for i in range(2)]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        c[i][j] = max(c[i][j], a[i][k] + b[k][j])
  return c

def mat_ksm(mat, pw):
  # 构造单位矩阵 I, 使得 I * mat = mat
  res = [
    [0, -inf],
    [-inf, 0]
  ]
  while pw > 0:
    if pw & 1:
      res = max_plus_mult(res, mat)
    mat = max_plus_mult(mat, mat)
    pw >>= 1
  return res


# 转移矩阵
M = [
  [a // 2, b // 2],
  [a, b],
]

ans = max_plus_mult([[-inf, 0], [0, 0]], mat_ksm(M, n))

print(max(ans[0][0], ans[0][1]))