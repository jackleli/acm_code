#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n;
  std::cin >> n;
  std::vector<int> t(n + 1);
  for (int i = 1; i <= n; i++) {
    std::cin >> t[i];
  }
  std::vector<int> cyc(n + 1), tis(n + 1);
  int ts = 0;
  for (int i = 1; i <= n; i++) {
    if (cyc[i]) {
      continue;
    }
    int x = i;
    std::vector<int> path;
    while (!tis[x]) {
      path.emplace_back(x);
      tis[x] = ++ts;
      x = t[x];
    }
    if (cyc[x]) {
      for (auto c : path) {
        cyc[c] = cyc[x];
      }
    } else {
      int len = ts - tis[x] + 1;
      for (auto c : path) {
        cyc[c] = len;
      }
    }
  }
  for (int i = 1; i <= n; i++) {
    std::cout << cyc[i] << " \n"[i == n];
  }

  return 0;
}