#include <bits/stdc++.h>

using LL = long long;

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  
  int n, l, w;
  std::cin >> n >> l >> w;
  int ans = 0;
  for (int i = 0; i < n; i++) {
    int d;
    std::cin >> d;
    if (d >= l - w && d <= l + w) {
      ans++;
    }
  }
  std::cout << ans << '\n';

  return 0;
}