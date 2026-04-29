#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m, k;
  std::cin >> n >> m >> k;
  int64_t ans = 0, res = 0;
  std::vector<int> h(n);
  for (int i = 0; i < n; i++) {
    std::cin >> h[i];
    if (h[i] < k) {
      h[i] = 0;
    }
  }
  for (int i = 0; i < n; i++) {
    res += h[i];
    if (i >= m - 1) {
      ans = std::max(ans, res);
      res -= h[i - m + 1];
    }
  }
  std::cout << ans << '\n';

  return 0;
}