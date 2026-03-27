#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n;
  std::cin >> n;
  std::vector<int> h(n);
  for (auto& hi : h) {
    std::cin >> hi;
  }
  std::vector<int> stk;
  int64_t ans = 0;
  for (int i = 0; i < n; i++) {
    while (stk.size() && stk.back() <= h[i]) {
      stk.pop_back();
    }
    ans += stk.size();
    stk.emplace_back(h[i]);
  }
  std::cout << ans << '\n';

  return 0;
}