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

    __asm__ __volatile__("addi x5, x0, 0" : : : "x5");
    __asm__ __volatile__("addi x6, x0, 0" : : : "x6");
    __asm__ __volatile__("addi x7, x0, 1" : : : "x7");

    for (int i = 0; i < iterations; i++) {
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");

        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");

        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");

        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");
        __asm__ __volatile__("div x5, x6, x7" : : : "x5");        
    }

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    return 0;
}