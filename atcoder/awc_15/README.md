## python技巧

1. python的 `defaultdict` 用法
  ```python
  from collections import defaultdict
  mp_int = defaultdict(int)
  mp_list = defaultdict(list)
  # 多维defaultdict创建例子:
  # 由于defaultdict要求参数是一个可调用的无参可调用对象: defaultdict(X), 比如函数、lambda，所以这里得使用lambda返回defaultdict(int)
  # 当defaultdict不存在键时，会自动调用 X() 构造键默认值
  mp_dims = defaultdict(lambda: defaultdict(int))
  mp_dims[3][4] += 12
  ```
2. python线段树模板
  ```python
  class Tag:
    def __init__(self, lazy: int = 0):
      self.lazy = lazy

    def apply(self, v: "Tag"):
      self.lazy += v.lazy

  class Info:
    def __init__(self, sum: int = 0, len: int = 0):
      self.sum = sum
      self.len = len

    def apply(self, v: Tag):
      self.sum += v.lazy * self.len

    def __add__(self, other: "Info") -> "Info":
      res = Info()
      res.sum = self.sum + other.sum
      res.len = self.len + other.len
      return res

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
        return
      mid = (l + r) >> 1
      self.build(u << 1, l, mid)
      self.build(u << 1 | 1, mid + 1, r)
      self.pull(u)
    
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
        return self.tree[u]
      self.push(u)
      mid = (l + r) >> 1
      if qr <= mid:
        return self.query(u << 1, l, mid, ql, qr)
      elif ql > mid:
        return self.query(u << 1 | 1, mid + 1, r, ql, qr)
      return self.query(u << 1, l, mid, ql, qr) + self.query(u << 1 | 1, mid + 1, r, ql, qr)
  ```