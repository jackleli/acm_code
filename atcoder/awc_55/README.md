## Asan

-fsanitize=address 是 GCC/Clang 编译器内置的内存检测工具（Google 开发），不需要额外安装软件，编译时加这个参数，程序运行时会自动监控所有内存读写。一旦触发内存非法操作（越界、空指针、野指针等），程序会立刻终止，并直接打印：错误类型 + 代码行号 + 越界细节，不用调试，一眼定位问题。

`g++ D.cpp -o D -std=c++20 -g -fsanitize=address`