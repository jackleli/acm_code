#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m;
  std::cin >> n >> m;
  std::vector<int> d(n);
  std::vector<std::vector<int>> g(n);
  for (int i = 0; i < n; i++) {
    int t;
    std::cin >> t;
    d[i] = t;
  }
  for (int i = 0; i < m; i++) {
    int u, v;
    std::cin >> u >> v;
    u -= 1, v -= 1;
    g[u].emplace_back(v);
    d[v] -= 1;
  }
  std::queue<int> q;
  std::vector<int8_t> vis(n);
  for (int i = 0; i < n; i++) {
    if (d[i] < 0) {
      q.push(i);
      vis[i] = 1;
    }
  }
  while (q.size()) {
    int u = q.front();
    q.pop();
    for (auto v : g[u]) {
      if (--d[v] < 0 && !vis[v]) {
        vis[v] = 1;
        q.push(v);
      }
    }
  }
  std::vector<int> ans;
  for (int i = 0; i < n; i++) {
    if (vis[i]) {
      ans.emplace_back(i + 1);
    }
  }
  if (ans.size() == 0) {
    std::cout << -1 << '\n';
  }
  for (int i = 0; i < ans.size(); i++) {
    std::cout << ans[i] << " \n"[i + 1 == ans.size()];
  }

  return 0;
}