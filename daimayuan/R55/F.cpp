#include <bits/stdc++.h>

constexpr int MAXN = 30;

template <int32_t kMod>
struct ModInt {
  int32_t val;
  ModInt() : val(0) {}
  ModInt(int64_t x) {
    x %= kMod;
    if (x >= kMod) {
      x -= kMod;
    }
    if (x < 0) {
      x += kMod;
    }
    val = x;
  }
  int32_t value() const { return val; }
  ModInt pow(int64_t b) const {
    ModInt res(1);
    ModInt a = *this;
    while (b) {
      if (b & 1) {
        res *= a;
      }
      a *= a;
      b >>= 1;
    }
    return res;
  }
  ModInt inv() const { return pow(kMod - 2); }
  ModInt operator+(const ModInt& rhs) const { return ModInt(val + rhs.val); }
  ModInt operator-(const ModInt& rhs) const { return ModInt(val - rhs.val); }
  ModInt operator*(const ModInt& rhs) const {
    return ModInt(int64_t(val) * rhs.val);
  }
  ModInt operator/(const ModInt& rhs) const { return *this * rhs.inv(); }
  ModInt& operator+=(const ModInt& rhs) { return *this = *this + rhs; }
  ModInt& operator-=(const ModInt& rhs) { return *this = *this - rhs; }
  ModInt& operator*=(const ModInt& rhs) { return *this = *this * rhs; }
  ModInt& operator/=(const ModInt& rhs) { return *this = *this / rhs; }
  friend std::ostream& operator<<(std::ostream& os, const ModInt& x) {
    return os << x.val;
  }
  friend std::istream& operator>>(std::istream& is, ModInt& x) {
    int64_t val;
    is >> val;
    x = ModInt(val);
    return is;
  }
  friend ModInt operator+(int64_t x, const ModInt& rhs) {
    return ModInt(x) + rhs;
  }
  friend ModInt operator-(int64_t x, const ModInt& rhs) {
    return ModInt(x) - rhs;
  }
  friend ModInt operator*(int64_t x, const ModInt& rhs) {
    return ModInt(x) * rhs;
  }
  friend ModInt operator/(int64_t x, const ModInt& rhs) {
    return ModInt(x) / rhs;
  }
};

using Mint = ModInt<998244353>;

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n;
  std::cin >> n;
  std::vector<int> a(n + 1);
  const Mint inv2 = Mint(2).inv();
  for (int i = 1; i <= n; i++) {
    std::cin >> a[i];
  }
  std::vector<std::vector<int>> g(n + 1);
  for (int i = 1; i < n; i++) {
    int u, v;
    std::cin >> u >> v;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  Mint ans = 0;
  auto dfs = [&](auto&& self, int u, int fa,
                 int w) -> std::array<std::array<Mint, 2>, MAXN> {
    std::array<std::array<Mint, 2>, MAXN> fu{};
    std::array<std::array<Mint, 2>, MAXN> tmp{};
    for (int i = 0; i < MAXN; i++) {
      fu[i][a[u] >> i & 1] += 1;
    }
    for (auto v : g[u]) {
      if (v == fa) {
        continue;
      }
      auto fv = self(self, v, u, a[u]);
      for (int i = 0; i < MAXN; i++) {
        if (w >> i & 1) {
          ans += tmp[i][1] * fv[i][1] * (1 << i);
          ans += tmp[i][0] * fv[i][0] * (1 << i);
          ans += fu[i][1] * fv[i][1] * fv[i][0] * (1 << i);
          ans += fu[i][0] * fv[i][1] * (fv[i][1] - 1) * inv2 * (1 << i);
          ans += fu[i][0] * fv[i][0] * (fv[i][0] - 1) * inv2 * (1 << i);
        } else {
          ans += tmp[i][0] * fv[i][1] * (1 << i);
          ans += tmp[i][1] * fv[i][0] * (1 << i);
          ans += fu[i][0] * fv[i][0] * fv[i][1] * (1 << i);
          ans += fu[i][1] * fv[i][1] * (fv[i][1] - 1) * inv2 * (1 << i);
          ans += fu[i][1] * fv[i][0] * (fv[i][0] - 1) * inv2 * (1 << i);
        }
        tmp[i][0] += fu[i][0] * fv[i][0];
        tmp[i][0] += fu[i][1] * fv[i][1];
        tmp[i][0] += fv[i][1] * (fv[i][1] - 1) * inv2;
        tmp[i][0] += fv[i][0] * (fv[i][0] - 1) * inv2;
        tmp[i][1] += fu[i][1] * fv[i][0];
        tmp[i][1] += fu[i][0] * fv[i][1];
        tmp[i][1] += fv[i][1] * fv[i][0];
        fu[i][0] += fv[i][0];
        fu[i][1] += fv[i][1];
      }
    }
    return fu;
  };
  dfs(dfs, 1, 0, 0);
  std::cout << ans << '\n';

  return 0;
}