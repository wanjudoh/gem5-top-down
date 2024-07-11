#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[]) {
    int iterations;
    if (argc == 2) {
        iterations = stoi(string(argv[1]));
    } else {
        cout << "Please provide the number of iterations.\n";
    }

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    __asm__ __volatile__("fsub.d f0, f0, f0");
    __asm__ __volatile__("fsub.d f1, f1, f1");
    __asm__ __volatile__("fsub.d f2, f2, f2");
    __asm__ __volatile__("fsub.d f3, f3, f3");
    __asm__ __volatile__("fsub.d f4, f4, f4");
    __asm__ __volatile__("fsub.d f5, f5, f5");
    __asm__ __volatile__("fsub.d f6, f6, f6");
    __asm__ __volatile__("fsub.d f7, f7, f7");

    __asm__ __volatile__("addi x5, x0, 1");

    // converts a 64-bit signed integer into a double-precision floating-point number
    __asm__ __volatile__("fcvt.d.l f0, x5");
    __asm__ __volatile__("fcvt.d.l f1, x5");
    __asm__ __volatile__("fcvt.d.l f2, x5");
    __asm__ __volatile__("fcvt.d.l f3, x5");
    __asm__ __volatile__("fcvt.d.l f4, x5");
    __asm__ __volatile__("fcvt.d.l f5, x5");
    __asm__ __volatile__("fcvt.d.l f6, x5");
    __asm__ __volatile__("fcvt.d.l f7, x5");

    for (int i = 0; i < iterations; i++) {
        __asm__ __volatile__("fmul.d f0, f0, f0");
        __asm__ __volatile__("fmul.d f1, f1, f1");
        __asm__ __volatile__("fmul.d f2, f2, f2");
        __asm__ __volatile__("fmul.d f3, f3, f3");
        __asm__ __volatile__("fmul.d f4, f4, f4");
        __asm__ __volatile__("fmul.d f5, f5, f5");
        __asm__ __volatile__("fmul.d f6, f6, f6");
        __asm__ __volatile__("fmul.d f7, f7, f7");

        __asm__ __volatile__("fmul.d f0, f0, f0");
        __asm__ __volatile__("fmul.d f1, f1, f1");
        __asm__ __volatile__("fmul.d f2, f2, f2");
        __asm__ __volatile__("fmul.d f3, f3, f3");
        __asm__ __volatile__("fmul.d f4, f4, f4");
        __asm__ __volatile__("fmul.d f5, f5, f5");
        __asm__ __volatile__("fmul.d f6, f6, f6");
        __asm__ __volatile__("fmul.d f7, f7, f7");

        __asm__ __volatile__("fmul.d f0, f0, f0");
        __asm__ __volatile__("fmul.d f1, f1, f1");
        __asm__ __volatile__("fmul.d f2, f2, f2");
        __asm__ __volatile__("fmul.d f3, f3, f3");
        __asm__ __volatile__("fmul.d f4, f4, f4");
        __asm__ __volatile__("fmul.d f5, f5, f5");
        __asm__ __volatile__("fmul.d f6, f6, f6");
        __asm__ __volatile__("fmul.d f7, f7, f7");

        __asm__ __volatile__("fmul.d f0, f0, f0");
        __asm__ __volatile__("fmul.d f1, f1, f1");
        __asm__ __volatile__("fmul.d f2, f2, f2");
        __asm__ __volatile__("fmul.d f3, f3, f3");
        __asm__ __volatile__("fmul.d f4, f4, f4");
        __asm__ __volatile__("fmul.d f5, f5, f5");
        __asm__ __volatile__("fmul.d f6, f6, f6");
        __asm__ __volatile__("fmul.d f7, f7, f7");
    }

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    return 0;
}