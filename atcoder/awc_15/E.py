import math
from collections import defaultdict
from functools import cmp_to_key

N, Q = map(int, input().split())
P = [0] + list(map(int, input().split()))

qry = []

for i in range(Q):
  L, R = map(int, input().split())
  qry.append((L, R, i))

B = int(math.sqrt(N))

def cmp(x, y):
  bl_x = x[0] // B
  bl_y = y[0] // B
  if bl_x != bl_y:
    return bl_x - bl_y
  if bl_x % 2 == 1:
    return y[1] - x[1]
  return x[1] - y[1]

qry.sort(key=cmp_to_key(cmp))

l, r = 1, 0
mp = defaultdict(int)
cur = 0
ans = [0] * Q
def add(x):
  global cur
  mp[x] += 1
  if mp[x] == 1:
    cur += 1
def delx(x):
  global cur
  mp[x] -= 1
  if mp[x] == 0:
    cur -= 1
for L, R, idx in qry:
  while l > L:
    l -= 1
    add(P[l])
  while r < R:
    r += 1
    add(P[r])
  while l < L:
    delx(P[l])
    l += 1
  while r > R:
    delx(P[r])
    r -= 1
  ans[idx] = cur
print(*ans, sep="\n")
# class Tag:
#   def __init__(self, lazy: int = 0):
#     self.lazy = lazy

#   def apply(self, v: "Tag"):
#     self.lazy += v.lazy

# class Info:
#   def __init__(self, sum: int = 0, len: int = 0):
#     self.sum = sum
#     self.len = len

#   def apply(self, v: Tag):
#     self.sum += v.lazy * self.len

#   def __add__(self, other: "Info") -> "Info":
#     res = Info()
#     res.sum = self.sum + other.sum
#     res.len = self.len + other.len
#     return res

# class SegmentTree:
#   def __init__(self, n: int, info_list: list[Info]):
#     self.n = n
#     self.tree = [Info() for i in range(4 * n + 1)]
#     self.tag = [Tag() for i in range(4 * n + 1)]
#     self.info_list = info_list
#     self.build(1, 1, n)

#   def pull(self, u: int):
#     self.tree[u] = self.tree[u << 1] + self.tree[u << 1 | 1]

#   def push(self, u: int):
#     if self.tag[u] != Tag():
#       self.tree[u << 1].apply(self.tag[u])
#       self.tree[u << 1 | 1].apply(self.tag[u])
#       self.tag[u << 1].apply(self.tag[u])
#       self.tag[u << 1 | 1].apply(self.tag[u])
#       self.tag[u] = Tag()
  
#   def build(self, u: int, l: int, r: int):
#     if l == r:
#       self.tree[u] = self.info_list[l]
#       return
#     mid = (l + r) >> 1
#     self.build(u << 1, l, mid)
#     self.build(u << 1 | 1, mid + 1, r)
#     self.pull(u)
  
#   def modify(self, u: int, l: int, r: int, ql: int, qr: int, v: Tag):
#     if l >= ql and r <= qr:
#       self.tree[u].apply(v)
#       self.tag[u].apply(v)
#       return
#     self.push(u)
#     mid = (l + r) >> 1
#     if ql <= mid:
#       self.modify(u << 1, l, mid, ql, qr, v)
#     if qr > mid:
#       self.modify(u << 1 | 1, mid + 1, r, ql, qr, v)
#     self.pull(u)
  
#   def query(self, u: int, l: int, r: int, ql: int, qr: int) -> Info:
#     if l >= ql and r <= qr:
#       return self.tree[u]
#     self.push(u)
#     mid = (l + r) >> 1
#     if qr <= mid:
#       return self.query(u << 1, l, mid, ql, qr)
#     elif ql > mid:
#       return self.query(u << 1 | 1, mid + 1, r, ql, qr)
#     return self.query(u << 1, l, mid, ql, qr) + self.query(u << 1 | 1, mid + 1, r, ql, qr)


# info_list = [Info(0, 1) for i in range(N + 1)]
# seg_tree = SegmentTree(N, info_list)

# qry = [[] for i in range(N + 1)]
# for i in range(Q):
#   L, R = map(int, input().split())
#   qry[R].append([L, i])

# last = [0] * (N + 1)
# ans = [0] * Q

# for i in range(1, N + 1):
#   x = P[i]
#   seg_tree.modify(1, 1, N, last[x] + 1, i, Tag(1))
#   for l, idx in qry[i]:
#     ans[idx] = seg_tree.query(1, 1, N, l, l).sum
#   last[x] = i

# print(*ans, sep="\n")
