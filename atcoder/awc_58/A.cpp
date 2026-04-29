#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, p, t, c;
  std::cin >> n >> p >> t >> c;
  int mx = 0;
  for (int i = 0; i < n; i++) {
    int s;
    std::cin >> s;
    mx = std::max(mx, s);
  }
  if (p >= t) {
    std::cout << 0 << '\n';
  } else if (mx > p && mx >= t) {
    std::cout << c << '\n';
  } else {
    std::cout << -1 << '\n';
  }

  return 0;
}