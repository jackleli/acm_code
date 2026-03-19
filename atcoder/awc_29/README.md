## python用法记录
1. python中的 `deque`
```python
from collections import deque
dq = deque()

# 队尾插入
dq.append(1)
# 队尾批量插入
dq.extend([1, 22, 3])
# 队头插入
dq.appendleft(1)
# 队头批量插入
dq.extendleft([1, 22, 3])
# 队尾弹出并返回元素
x = d.pop()
# 队头弹出并返回元素
x = d.popleft()
# 清空
dq.clear()
# 转list
print(list(dq))
# 支持下标索引访问
for i in range(len(dq)):
  print(f"idx: {i}, val: {dq[i]}")
```