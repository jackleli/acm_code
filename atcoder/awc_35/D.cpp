#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m;
  std::cin >> n >> m;
  std::vector<int> v(n);
  for (auto& vi : v) {
    std::cin >> vi;
  }
  std::vector<int> dt(m);
  for (int i = 0; i < m; i++) {
    int d, t;
    std::cin >> d >> t;
    dt[i] = (d + t - 1) / t;
  }
  std::sort(dt.begin(), dt.end());
  std::sort(v.begin(), v.end());
  int ans = 0;
  for (int i = 0, j = 0; i < m; i++) {
    while (j < n && v[j] < dt[i]) {
      j++;
    }
    if (j == n) {
      break;
    }
    j += 1;
    ans++;
  }
  std::cout << ans << '\n';

  return 0;
}