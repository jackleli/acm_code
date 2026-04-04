#include <bits/stdc++.h>

constexpr int mod = 998244353;

int main() {
  int n, k;
  std::cin >> n >> k;

  std::vector<int> f(n + 1), inv(n + 1), finv(n + 1), pw2(n + 1);
  f[0] = f[1] = inv[1] = finv[0] = finv[1] = 1;
  pw2[0] = 1, pw2[1] = 2;
  for (int i = 2; i <= n; i++) {
    f[i] = 1LL * f[i - 1] * i % mod;
    inv[i] = 1LL * (mod - mod / i) * inv[mod % i] % mod;
    finv[i] = 1LL * finv[i - 1] * inv[i] % mod;
    pw2[i] = 2LL * pw2[i - 1] % mod;
  }
  auto C = [&](int a, int b) -> int {
    if (b < 0 || a < b) {
      return 0;
    }
    return 1LL * f[a] * finv[b] % mod * finv[a - b] % mod;
  };
  int smart = 0, confused = 0;
  for (int i = 2; i <= n; i++) {
    std::cout << "? " << i << ' ' << 1 << std::endl;
    int x;
    std::cin >> x;
    if (x == 1) {
      smart++;
    } else {
      confused++;
    }
  }
  if (smart < confused) {
    std::swap(smart, confused);
    confused++;
  } else {
    smart++;
  }
  int ans = 0;
  for (int i = 0; i <= confused; i++) {
    if (i > k || k - i > smart) {
      continue;
    }
    int c = confused - i + k - i;
    ans = (ans + 1LL * pw2[c] * C(confused, i) % mod * C(smart, k - i) % mod) % mod;
  }
  std::cout << "! " << ans << std::endl;

  return 0;
}