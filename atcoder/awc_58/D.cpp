#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m, k;
  std::cin >> n >> m >> k;
  std::vector<std::vector<std::array<int, 2>>> g(n + 1);
  while (m--) {
    int u, v, w;
    std::cin >> u >> v >> w;
    g[u].push_back({v, w});
    g[v].push_back({u, w});
  }
  std::priority_queue<std::pair<int64_t, int>, std::vector<std::pair<int64_t, int>>, std::greater<>> pq;
  constexpr int64_t inf = 1e18;
  std::vector<int64_t> dis(n + 1, inf);
  std::vector<int8_t> vis(n + 1);
  dis[k] = 0;
  pq.push({0, k});
  while (pq.size()) {
    auto [d, u] = pq.top();
    pq.pop();
    if (vis[u]) {
      continue;
    }
    vis[u] = true;
    for (auto [v, w] : g[u]) {
      if (dis[v] > dis[u] + w) {
        dis[v] = dis[u] + w;
        pq.push({dis[v], v});
      }
    }
  }
  if (dis[1] == inf || dis[n] == inf) {
    std::cout << -1 << '\n';
  } else {
    std::cout << dis[1] + dis[n] << '\n';
  }

  return 0;
}