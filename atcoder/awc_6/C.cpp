
#include <bits/stdc++.h>

using LL = long long;

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m, d;
  std::cin >> n >> m >> d;
  LL ans = 0;
  for (int i = 0; i < n; i++) {
    int t;
    std::cin >> t;
    if (t <= m) {
      continue;
    }
    // t - dk <= m
    // dk >= t - m
    ans += (t - m + d - 1) / d;
  }
  std::cout << ans << '\n';

  return 0;
} 