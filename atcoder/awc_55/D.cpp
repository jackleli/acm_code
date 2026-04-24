#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int q;
  std::cin >> q;
  std::multiset<int> s1, s2;
  int ans = 0;
  auto balance = [&]() {
    while (s1.size() && s2.size() && *s1.rbegin() > *s2.begin()) {
      auto iter = --s1.end();
      s2.insert(*iter);
      s1.erase(iter);
    }
    while (s2.size() > s1.size()) {
      auto iter = s2.begin();
      s1.insert(*iter);
      s2.erase(iter);
    }
    while (s1.size() > s2.size() + 1) {
      auto iter = --s1.end();
      s2.insert(*iter);
      s1.erase(iter);
    }
  };
  auto mid_val = [&]() {
    return *s1.rbegin();
  };
  auto add = [&](int x) {
    s1.insert(x);
    balance();
  };
  auto del = [&](int x) {
    auto val = mid_val();
    if (auto iter = s1.find(x); iter != s1.end()) {
      ans += *iter == val;
      s1.erase(iter);
    } else if (auto iter = s2.find(x); iter != s2.end()) {
      ans += *iter == val;
      s2.erase(iter);
    }
    balance();
  };
  while (q--) {
    char op;
    int x;
    std::cin >> op >> x;
    if (op == '+') {
      add(x);
    } else {
      del(x);
    }
  }
  std::cout << ans << '\n';

  return 0;
}