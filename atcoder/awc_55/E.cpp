#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n;
  int64_t k;
  std::cin >> n >> k;
  std::vector<int64_t> a(n), b(n);
  for (int i = 0; i < n; i++) {
    std::cin >> a[i] >> b[i];
  }
  std::unordered_set<int64_t> se;
  auto dfs1 = [&](auto&& self, int u, int64_t sum) -> void {
    if (sum > k) {
      return;
    }
    if (u >= n / 2) {
      se.insert(sum);
      return;
    }
    self(self, u + 1, sum + a[u]);
    self(self, u + 1, sum + b[u]);
    self(self, u + 1, sum);
  };
  dfs1(dfs1, 0, 0);
  auto dfs2 = [&](auto&& self, int u, int64_t sum) -> bool {
    if (sum > k) {
      return false;
    }
    if (u == n) {
      return se.contains(k - sum);
    }
    return  self(self, u + 1, sum) || self(self, u + 1, sum + a[u]) || self(self, u + 1, sum + b[u]);
  };
  std::cout << (dfs2(dfs2, n / 2, 0) ? "Yes" : "No") << '\n';

  return 0;
}