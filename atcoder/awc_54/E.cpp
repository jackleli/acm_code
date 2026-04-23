#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m;
  std::cin >> n >> m;
  std::vector<int> tr(n + 1);
  auto add = [&](int x, int k) {
    for (int i = x; i <= n; i += i & -i) {
      tr[i] += k;
    }
  };
  auto ask = [&](int x) {
    int res = 0;
    for (int i = x; i; i -= i & -i) {
      res += tr[i];
    }
    return res;
  };
  for (int i = 1; i <= n; i++) {
    add(i, 1);
  }
  for (int i = 1; i <= m; i++) {
    int s;
    std::cin >> s;
    std::cout << ask(s) << '\n';
    add(s, -1);
  }

  return 0;
}