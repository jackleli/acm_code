#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, k, m;
  std::cin >> n >> k >> m;
  std::vector<int> s(n), p(m), cv(m);
  for (int i = 0; i < n; i++) {
    std::cin >> s[i];
  }
  for (int i = 0; i < m; i++) {
    int l, r;
    std::cin >> l >> r >> p[i];
    for (int j = l - 1; j < r; j++) {
      cv[i] |= 1 << j;  
    }
  }
  int ans = 0;
  for (int mask = 0; mask < 1 << n; mask++) {
    if (__builtin_popcount(mask) > k) {
      continue;
    }
    int res = 0;
    for (int i = 0; i < n; i++) {
      if (mask >> i & 1) {
        res += s[i];
      }
    }
    for (int i = 0; i < m; i++) {
      if ((mask & cv[i]) != 0) {
        res += p[i];
      }
    }
    ans = std::max(ans, res);
  }
  std::cout << ans << '\n';

  return 0;
}