#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m;
  std::cin >> n >> m;
  std::vector<int64_t> p(n);
  for (auto& pi : p) {
    std::cin >> pi;
  }
  for (int i = 0; i < m; i++) {
    int u, v, w;
    std::cin >> u >> v >> w;
    u -= 1, v -= 1;
    p[u] -= w, p[v] += w;
  }
  int maxv_id = 0;
  for (int i = 1; i < n; i++) {
    if (p[maxv_id] < p[i]) {
      maxv_id = i;
    }
  }
  std::cout << maxv_id + 1;

  return 0;
}