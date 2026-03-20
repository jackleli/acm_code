#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m;
  std::cin >> n >> m;
  std::vector<int> p(n), t(n);
  for (int i = 0; i < n; i++) {
    std::cin >> p[i] >> t[i];
  }
  for (int i = 0; i < m; i++) {
    int k;
    std::cin >> k;
    int min_ve = 1e9 + 1, min_me = 1e9 + 1;
    for (int j = 0; j < k; j++) {
      int s;
      std::cin >> s;
      s -= 1;
      if (!t[s]) {
        min_ve = std::min(min_ve, p[s]);
      } else {
        min_me = std::min(min_me, p[s]);
      }
    }
    if (min_ve == 1e9 + 1 || min_me == 1e9 + 1) {
      std::cout << -1 << '\n';
    } else {
      std::cout << min_ve + min_me << '\n';
    }
  }

  return 0;
}