#include <bits/stdc++.h>

int main() {
  int n, k;
  std::cin >> n >> k;
  std::vector<int> a(n);
  for (auto& ai : a) {
    std::cin >> ai;
  }
  std::list<int> l;
  std::unordered_map<int, std::list<int>::iterator> mp;
  std::vector<int> ans(n);
  for (int i = 0; i < n; i++) {
    auto iter = mp.find(a[i]);
    if (iter == mp.end()) {
      l.push_back(i);
      mp.emplace(a[i], --l.end());
    } else {
      auto p = iter->second;
      int cnt = 0;
      while (p != l.end() && cnt < k) {
        cnt += 1;
        ans[*p] = i + 1;
        mp.erase(a[*p]);
        p = l.erase(p);
      }
    }
  }
  for (int i = 0; i < n; i++) {
    std::cout << ans[i] << " \n"[i == n - 1];
  }

  return 0;
}