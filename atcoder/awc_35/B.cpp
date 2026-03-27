#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m;
  std::cin >> n >> m;
  std::vector<int> d(n), s(m);
  for (auto& di : d) {
    std::cin >> di;
  }
  for (auto& si : s) {
    std::cin >> si;
  }
  std::sort(s.begin(), s.end());
  int64_t ans = 0;
  for (int i = 0; i < n; i++) {
    int32_t cost = std::numeric_limits<int32_t>::max();
    auto iter = std::lower_bound(s.begin(), s.end(), d[i]);
    if (iter != s.end()) {
      cost = std::min(cost, *iter - d[i]);
    }
    if (iter != s.begin()) {
      cost = std::min(cost, d[i] - *(--iter));
    }
    ans += cost;
  }
  std::cout << ans << '\n';

  return 0;
}