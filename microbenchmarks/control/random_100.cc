#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(int argc, char *argv[]) {
    int iterations;
    if (argc == 2) {
        iterations = stoi(string(argv[1]));
    } else {
        cout << "Please provide the number of iterations.\n";
    }

    unsigned long long jump = 1;
    unsigned long long lfsr = 0x80000000;
    unsigned long long bit;

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    for (int i = 0; i < iterations; i++) {
        bit  = ~((lfsr >> 0) ^ (lfsr >> 10) ^ (lfsr >> 11) ^ (lfsr >> 30) ) & 1;
        lfsr =  (lfsr >> 1) | (bit << 31);
        jump = lfsr & 1;
        if (jump)   __asm__ __volatile__("addi %0, %0, 0" : "=r" (bit) : "0" (bit) : );
        else        __asm__ __volatile__("addi %0, %0, 0" : "=r" (lfsr) : "0" (lfsr) : );

        /// Linear Feedback Shift Register
        bit  = ~((lfsr >> 0) ^ (lfsr >> 10) ^ (lfsr >> 11) ^ (lfsr >> 30) ) & 1;
        lfsr =  (lfsr >> 1) | (bit << 31);
        jump = lfsr & 1;
        if (jump)   __asm__ __volatile__("addi %0, %0, 0" : "=r" (bit) : "0" (bit) : );
        else        __asm__ __volatile__("addi %0, %0, 0" : "=r" (lfsr) : "0" (lfsr) : );

        /// Linear Feedback Shift Register
        bit  = ~((lfsr >> 0) ^ (lfsr >> 10) ^ (lfsr >> 11) ^ (lfsr >> 30) ) & 1;
        lfsr =  (lfsr >> 1) | (bit << 31);
        jump = lfsr & 1;
        if (jump)   __asm__ __volatile__("addi %0, %0, 0" : "=r" (bit) : "0" (bit) : );
        else        __asm__ __volatile__("addi %0, %0, 0" : "=r" (lfsr) : "0" (lfsr) : );

        /// Linear Feedback Shift Register
        bit  = ~((lfsr >> 0) ^ (lfsr >> 10) ^ (lfsr >> 11) ^ (lfsr >> 30) ) & 1;
        lfsr =  (lfsr >> 1) | (bit << 31);
        jump = lfsr & 1;
        if (jump)   __asm__ __volatile__("addi %0, %0, 0" : "=r" (bit) : "0" (bit) : );
        else        __asm__ __volatile__("addi %0, %0, 0" : "=r" (lfsr) : "0" (lfsr) : );
    }

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    return 0;
}