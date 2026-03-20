#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, k;
  std::cin >> n >> k;
  int ans = 0, len = 0;
  for (int i = 0; i < n; i++) {
    int x;
    std::cin >> x;
    if (x) {
      len++;
    } else {
      ans += len >= k;
      len = 0;
    }
  }
  ans += len >= k;
  std::cout << ans << '\n';

  return 0;
}