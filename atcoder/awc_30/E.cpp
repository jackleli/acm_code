#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n;
  std::cin >> n;
  std::vector<int> a(n);
  int MAXN = 0;
  for (int i = 0; i < n; i++) {
    std::cin >> a[i];
    MAXN = std::max(MAXN, a[i]);
  }
  std::vector<int> cnt(MAXN + 1);
  for (int i = 0; i < n; i++) {
    cnt[a[i]]++;
  }
  int64_t ans = 0;
  for (int d = 1; d <= MAXN; d++) {
    int k = 0;
    for (int m = d; m <= MAXN; m += d) {
      k += cnt[m];
    }
    ans = std::max(ans, int64_t(d) * k);
  }
  std::cout << ans << '\n';

  return 0;
}