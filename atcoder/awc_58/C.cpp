#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m, k;
  std::cin >> n >> m >> k;
  std::vector<int> c(n + 1);
  for (int i = 1; i <= m; i++) {
    int l, r;
    std::cin >> l >> r;
    c[l] += 1;
    if (r < n) {
      c[r + 1] -= 1;
    }
  }
  int ans = 0;
  for (int i = 1; i <= n; i++) {
    c[i] += c[i - 1];
    ans += c[i] >= k;
  }
  std::cout << ans << '\n';

  return 0;
}