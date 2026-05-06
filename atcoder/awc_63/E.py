
class Tag:
  def __init__(self, lazy: int = 0):
    self.lazy = lazy

  def apply(self, v: "Tag"):
    self.lazy = v.lazy

  # 注意python里面的 == 对于类默认比较的是内存地址，如果需要比较值需要重写==
  def __eq__(self, other):
    if isinstance(other, Tag):
      return self.lazy == other.lazy
    return False

class Info:
  def __init__(self, cnt: int = 0, cl: int = 0, cr: int = 0):
    self.cnt = cnt
    self.cl = cl
    self.cr = cr
  
  def __add__(self, other: "Info") -> "Info":
    res = Info()
    res.cnt = self.cnt + other.cnt - (self.cr == other.cl)
    res.cl = self.cl
    res.cr = other.cr
    return res
  
  def apply(self, v: Tag):
    self.cl = self.cr = v.lazy
    self.cnt = 1

class SegmentTree:
  def __init__(self, n: int, info_list: list[Info]):
    self.n = n
    self.tree = [Info() for i in range(4 * n + 1)]
    self.tag = [Tag() for i in range(4 * n + 1)]
    self.info_list = info_list
    self.build(1, 1, n)

  def pull(self, u: int):
    self.tree[u] = self.tree[u << 1] + self.tree[u << 1 | 1]

  def push(self, u: int):
    if self.tag[u] != Tag():
      self.tree[u << 1].apply(self.tag[u])
      self.tree[u << 1 | 1].apply(self.tag[u])
      self.tag[u << 1].apply(self.tag[u])
      self.tag[u << 1 | 1].apply(self.tag[u])
      self.tag[u] = Tag()
  
  def build(self, u: int, l: int, r: int):
    if l == r:
      self.tree[u] = self.info_list[l]
      # print(u, l, r, self.tree[u].cnt, self.tree[u].cl, self.tree[u].cr)
      return
    mid = (l + r) >> 1
    self.build(u << 1, l, mid)
    self.build(u << 1 | 1, mid + 1, r)
    self.pull(u)
    # print(u, l, r, self.tree[u].cnt, self.tree[u].cl, self.tree[u].cr)

  def modify(self, u: int, l: int, r: int, ql: int, qr: int, v: Tag):
    if l >= ql and r <= qr:
      self.tree[u].apply(v)
      self.tag[u].apply(v)
      return
    self.push(u)
    mid = (l + r) >> 1
    if ql <= mid:
      self.modify(u << 1, l, mid, ql, qr, v)
    if qr > mid:
      self.modify(u << 1 | 1, mid + 1, r, ql, qr, v)
    self.pull(u)

  def query(self, u: int, l: int, r: int, ql: int, qr: int) -> Info:
    if l >= ql and r <= qr:
      # print(u, l, r, self.tree[u].cnt, self.tree[u].cl, self.tree[u].cr)
      return self.tree[u]
    self.push(u)
    mid = (l + r) >> 1
    if qr <= mid:
      return self.query(u << 1, l, mid, ql, qr)
    elif ql > mid:
      return self.query(u << 1 | 1, mid + 1, r, ql, qr)
    return self.query(u << 1, l, mid, ql, qr) + self.query(u << 1 | 1, mid + 1, r, ql, qr)


n, q = map(int, input().split())
c = [0] + list(map(int, input().split()))
info_list = [Info(1, c[i], c[i]) for i in range(n + 1)]
seg_tree = SegmentTree(n, info_list)
# print(seg_tree.query(1, 1, n, 2, 5).cnt)

for i in range(q):
  opt = list(map(int, input().split()))
  if opt[0] == 1:
    seg_tree.modify(1, 1, n, opt[1], opt[2], Tag(opt[3]))
  else:
    print(seg_tree.query(1, 1, n, opt[1], opt[2]).cnt)