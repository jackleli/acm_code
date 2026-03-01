#include <bits/stdc++.h>

using LL = long long;

constexpr LL inf = std::numeric_limits<LL>::min() / 2;

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  
  int n, m;
  std::cin >> n >> m;
  std::vector<std::array<int, 2>> seg(m);
  for (auto& [l, r] : seg) {
    std::cin >> l >> r;
  }
  std::sort(seg.begin(), seg.end());
  int ans = 0, st = 1;
  for (int i = 0; i < m; i++) {
    int j = i, max_r = 0;
    while (j < m && seg[j][0] <= st) {
      max_r = std::max(max_r, seg[j++][1]);
    }
    if (max_r < st) {
      std::cout << -1 << '\n';
      return 0;
    }
    ans++;
    st = max_r + 1;
    if (st > n) {
      break;
    }
    i = j - 1;
  }
  if (st <= n) {
    ans = -1;
  }
  std::cout << ans << '\n';

  return 0;
}