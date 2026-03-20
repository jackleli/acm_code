#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m;
  std::cin >> n >> m;
  for (int i = 0; i < n; i++) {
    int a;
    std::cin >> a;
    std::cout << a / m << ' ' << a % m << '\n';
  }

  return 0;
}