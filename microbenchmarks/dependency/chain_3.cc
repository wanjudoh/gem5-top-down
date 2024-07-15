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

    int count0 = 0;
    int count1 = 0;
    int count2 = 0;

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    for (int i = 0; i < iterations; i++) {
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count0) : "0" (count0) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count1) : "0" (count1) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count2) : "0" (count2) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count0) : "0" (count0) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count1) : "0" (count1) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count2) : "0" (count2) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count0) : "0" (count0) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count1) : "0" (count1) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count2) : "0" (count2) : );

        __asm__ __volatile__("add x0, x0, x0" : "=r" (count0) : "0" (count0) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count1) : "0" (count1) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count2) : "0" (count2) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count0) : "0" (count0) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count1) : "0" (count1) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count2) : "0" (count2) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count0) : "0" (count0) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count1) : "0" (count1) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count2) : "0" (count2) : );

        __asm__ __volatile__("add x0, x0, x0" : "=r" (count0) : "0" (count0) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count1) : "0" (count1) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count2) : "0" (count2) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count0) : "0" (count0) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count1) : "0" (count1) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count2) : "0" (count2) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count0) : "0" (count0) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count1) : "0" (count1) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count2) : "0" (count2) : );

        __asm__ __volatile__("add x0, x0, x0" : "=r" (count0) : "0" (count0) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count1) : "0" (count1) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count2) : "0" (count2) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count0) : "0" (count0) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count1) : "0" (count1) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count2) : "0" (count2) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count0) : "0" (count0) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count1) : "0" (count1) : );
        __asm__ __volatile__("add x0, x0, x0" : "=r" (count2) : "0" (count2) : );
    }

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    return 0;
}