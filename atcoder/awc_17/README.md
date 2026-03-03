### python用法记录
1. 对于一个int数x求其二进制1的个数，可以直接用 `x.bit_count()`
2. 对于遍历数组条件求和，可以使用类似 `sum(a[i] for i in range(n) if mask >> i & 1)`
3. python的解包遍历: `for u, v, w in edge:`
4. `print(*a, sep=" ")`, sep 可以设置列表输出的分隔符号
5. 创建多维数组: `a = [[10**9 for i in range(n)] for i in range(n)]`
6. python里面，对于两个可变类(list, dict, set)，执行 `x = y`，是浅拷贝，对于不可变类型(int, str, tuple, float, bool)，执行 `x = y` 是深拷贝
7. 使用 copy 的 deepcopy 可以实现可变类型的深拷贝
    ```
    import copy
    a = [[1, 2], [3, 4]]
    b = copy.deepcopy(b)
    ```