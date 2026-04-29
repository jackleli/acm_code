#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, k;
  std::cin >> n >> k;
  std::vector<int> a(n);
  for (int i = 0; i < n; i++) {
    std::cin >> a[i];
  }
  std::multiset<int> se;
  int ans = 0;
  for (int i = 0, j = 0; i < n; i++) {
    se.insert(a[i]);
    while (j < n && *se.rbegin() - *se.begin() > k) {
      se.erase(se.find(a[j++]));
    }
    ans = std::max(ans, i - j + 1);
  }
  std::cout << ans << '\n';

  return 0;
}