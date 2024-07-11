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

    // converts a 64-bit signed integer into a double-precision floating-point number
    __asm__ __volatile__("fcvt.d.l f0, x0");
    __asm__ __volatile__("fcvt.d.l f1, x0");
    __asm__ __volatile__("fcvt.d.l f2, x0");
    __asm__ __volatile__("fcvt.d.l f3, x0");
    __asm__ __volatile__("fcvt.d.l f4, x0");
    __asm__ __volatile__("fcvt.d.l f5, x0");
    __asm__ __volatile__("fcvt.d.l f6, x0");
    __asm__ __volatile__("fcvt.d.l f7, x0");

    for (int i = 0; i < iterations; i++) {
        __asm__ __volatile__("fadd.d f0, f0, f0");
        __asm__ __volatile__("fadd.d f1, f1, f1");
        __asm__ __volatile__("fadd.d f2, f2, f2");
        __asm__ __volatile__("fadd.d f3, f3, f3");
        __asm__ __volatile__("fadd.d f4, f4, f4");
        __asm__ __volatile__("fadd.d f5, f5, f5");
        __asm__ __volatile__("fadd.d f6, f6, f6");
        __asm__ __volatile__("fadd.d f7, f7, f7");

        __asm__ __volatile__("fadd.d f0, f0, f0");
        __asm__ __volatile__("fadd.d f1, f1, f1");
        __asm__ __volatile__("fadd.d f2, f2, f2");
        __asm__ __volatile__("fadd.d f3, f3, f3");
        __asm__ __volatile__("fadd.d f4, f4, f4");
        __asm__ __volatile__("fadd.d f5, f5, f5");
        __asm__ __volatile__("fadd.d f6, f6, f6");
        __asm__ __volatile__("fadd.d f7, f7, f7");

        __asm__ __volatile__("fadd.d f0, f0, f0");
        __asm__ __volatile__("fadd.d f1, f1, f1");
        __asm__ __volatile__("fadd.d f2, f2, f2");
        __asm__ __volatile__("fadd.d f3, f3, f3");
        __asm__ __volatile__("fadd.d f4, f4, f4");
        __asm__ __volatile__("fadd.d f5, f5, f5");
        __asm__ __volatile__("fadd.d f6, f6, f6");
        __asm__ __volatile__("fadd.d f7, f7, f7");

        __asm__ __volatile__("fadd.d f0, f0, f0");
        __asm__ __volatile__("fadd.d f1, f1, f1");
        __asm__ __volatile__("fadd.d f2, f2, f2");
        __asm__ __volatile__("fadd.d f3, f3, f3");
        __asm__ __volatile__("fadd.d f4, f4, f4");
        __asm__ __volatile__("fadd.d f5, f5, f5");
        __asm__ __volatile__("fadd.d f6, f6, f6");
        __asm__ __volatile__("fadd.d f7, f7, f7");
    }

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    return 0;
}