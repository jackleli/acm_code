#include <bits/stdc++.h>

using LL = long long;

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, k;
  LL t;
  std::cin >> n >> k >> t;
  for (int i = 0; i < n; i++) {
    int d, r;
    std::cin >> d >> r;
    if (r >= 1LL * k * d) {
      t -= r;
    }
  }
  std::cout << (t <= 0 ? "Yes" : "No") << '\n';
  
  return 0;
}