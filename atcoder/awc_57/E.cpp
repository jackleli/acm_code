#include <bits/stdc++.h>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n;
  std::cin >> n;
  std::vector<int> p(n), v(n), ord(n);
  for (int i = 0; i < n; i++) {
    std::cin >> p[i] >> v[i];
    ord[i] = i;
  }
  std::sort(ord.begin(), ord.end(), [&](int x, int y) { return p[x] < p[y]; });
  std::vector<int> vtmp(n);
  for (int i = 0; i < n; i++) {
    vtmp[i] = v[ord[i]];
  }
  v.swap(vtmp);
  auto calc = [&](auto&& self, int l, int r) -> int64_t {
    if (l >= r) {
      return 0;
    }
    int mid = (l + r) >> 1;
    int64_t ans = 0;
    ans += self(self, l, mid);
    ans += self(self, mid + 1, r);
    std::vector<int> vtmp;
    vtmp.reserve(r - l + 1);
    int i = l, j = mid + 1;
    while (i <= mid && j <= r) {
      if (v[i] <= v[j]) {
        vtmp.emplace_back(v[i++]);
      } else {
        ans += mid - i + 1;
        vtmp.emplace_back(v[j++]);
      }
    }
    while (i <= mid) {
      vtmp.emplace_back(v[i++]);
    }
    while (j <= r) {
      vtmp.emplace_back(v[j++]);
    }
    for (int i = l; i <= r; i++) {
      v[i] = vtmp[i - l];
    }
    return ans;
  };
  std::cout << calc(calc, 0, n - 1) << '\n';

  return 0;
}