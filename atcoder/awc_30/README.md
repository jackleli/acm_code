## trick 记录

1. 基环树找环, 且对于每个点都要输出其所在基环树的环长

```c++
// 法一: 首先对于任意一棵基环树，第一次找任意一个树上的点 u，其一次遍历一定能找到环和环长， 此时将环上的点入队，BFS反向/遍历传播cyc_len到树上所有节点即可，此时下次开始找的必然是一棵新的基环树

int n;
std::cin >> n;
std::vector<int> t(n + 1);
std::vector<std::vector<int>> g(n + 1);
for (int i = 1; i <= n; i++) {
  std::cin >> t[i];
  g[t[i]].push_back(i);
}
std::vector<int> cyc(n + 1), tis(n + 1);
int ts = 0;
for (int i = 1; i <= n; i++) {
  if (cyc[i]) {
    continue;
  }
  int x = i;
  std::vector<int> stk;
  while (!tis[x]) {
    stk.push_back(x);
    tis[x] = ++ts;
    x = t[x];
  }
  int len = ts - tis[x] + 1;
  std::queue<int> q;
  while (stk.size()) {
    int y = stk.back();
    stk.pop_back();
    cyc[y] = len;
    q.push(y);
    if (y == x) {
      break;
    }
  }
  while (q.size()) {
    int u = q.front();
    q.pop();
    for (auto v : g[u]) {
      if (!cyc[v]) {
        cyc[v] = cyc[u];
        q.push(v);
      }
    }
  }
}
for (int i = 1; i <= n; i++) {
  std::cout << cyc[i] << " \n"[i == n];
}


// 法二: 直接对于每个点都去遍历，设置vis[u] = 0, 1, 2 这三种状态，vis[u] = 2 表示这个点已经知道所在基环树的环长，直接跳过，否则为 vis[u] = 0, 1 两种情况，继续从 u 遍历直到 vis[u] != 0，此时u停在的点只有两种情况一种是 vis[u] = 1，一种是 vis[u] = 2，如果是第一种说明找到了一个新的基环树的环，此时算出环长，直接遍历path传播环长，否则说明是已经找到基环树的环，此时应该直接取到cyc_len遍历path路径的点直接传播

int n;
std::cin >> n;
std::vector<int> t(n + 1);
for (int i = 1; i <= n; i++) {
  std::cin >> t[i];
}
std::vector<int> cyc(n + 1), tis(n + 1);
int ts = 0;
for (int i = 1; i <= n; i++) {
  if (cyc[i]) {
    continue;
  }
  int x = i;
  std::vector<int> path;
  while (!tis[x]) {
    path.emplace_back(x);
    tis[x] = ++ts;
    x = t[x];
  }
  if (cyc[x]) {
    for (auto c : path) {
      cyc[c] = cyc[x];
    }
  } else {
    int len = ts - tis[x] + 1;
    for (auto c : path) {
      cyc[c] = len;
    }
  }
}
for (int i = 1; i <= n; i++) {
  std::cout << cyc[i] << " \n"[i == n];
}

```