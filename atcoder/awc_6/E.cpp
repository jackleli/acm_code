#include <bits/stdc++.h>

using LL = long long;

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  
  int n, q;
  std::cin >> n >> q;
  std::vector<int> s(n + 1);
  std::vector<LL> tr(n + 1);
  auto add = [&](int x, int v) {
    for (int i = x; i <= n; i += i & -i) {
      tr[i] += v;
    }
  };
  auto ask = [&](int x) {
    LL res = 0;
    for (int i = x; i > 0; i -= i & -i) {
      res += tr[i];
    }
    return res;
  };
  auto ask_range = [&](int l, int r) {
    return ask(r) - ask(l - 1);
  };
  for (int i = 1; i <= n; i++) {
    std::cin >> s[i];
    add(i, s[i]);
  }
  while (q--) {
    int t;
    std::cin >> t;
    if (t == 1) {
      int l, r;
      std::cin >> l >> r;
      std::cout << ask_range(l, r) << '\n';
    } else {
      int x, v;
      std::cin >> x >> v;
      add(x, v - s[x]);
      s[x] = v;
    }
  }
  
  return 0;
}