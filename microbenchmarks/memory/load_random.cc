#include <iostream>
#include <string>
#include <ctime>

using namespace std;

struct list {
    int value;
    char pad[26];
};

typedef struct list element;

int main(int argc, char *argv[]) {
    int iterations;
    int size;
    if (argc == 3) {
        iterations = stoi(string(argv[1]));
        size = stoi(string(argv[2]));

        if (size % 32 != 0) {
            cout << "The array size needs to be divisible by 32 (due to unrolling)\n";
        }
    } else {
        cout << "Please provide the number of iterations and array size\n";
    }

    element *ptr_list = nullptr;
    ptr_list = (element *)aligned_alloc(32, sizeof(element) * size);

    for (int i = 0; i < size; i++) {
        ptr_list[i].value = 1;
    }

    unsigned int i = 0, j = 0;
    unsigned int jump = 1;

    unsigned int count[32];
    for (i = 0; i < 32; i++) {
        count[i] = 0;
    }

    unsigned int lfsr = 0x80000000;
    unsigned bit;

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    for (i = 0; i < iterations; i++) {
        for (j = 0; j <= size; j += 32) {
            bit  = ~((lfsr >> 0) ^ (lfsr >> 10) ^ (lfsr >> 11) ^ (lfsr >> 30) ) & 1;
            lfsr =  (lfsr >> 1) | (bit << 31);

            jump = lfsr % (size - 32);
            count[0] += ptr_list[jump].value;
            count[1] += ptr_list[jump + 1].value;
            count[2] += ptr_list[jump + 2].value;
            count[3] += ptr_list[jump + 3].value;
            count[4] += ptr_list[jump + 4].value;
            count[5] += ptr_list[jump + 5].value;
            count[6] += ptr_list[jump + 6].value;
            count[7] += ptr_list[jump + 7].value;

            count[8] += ptr_list[jump + 8].value;
            count[9] += ptr_list[jump + 9].value;
            count[10] += ptr_list[jump + 10].value;
            count[11] += ptr_list[jump + 11].value;
            count[12] += ptr_list[jump + 12].value;
            count[13] += ptr_list[jump + 13].value;
            count[14] += ptr_list[jump + 14].value;
            count[15] += ptr_list[jump + 15].value;

            count[16] += ptr_list[jump + 16].value;
            count[17] += ptr_list[jump + 17].value;
            count[18] += ptr_list[jump + 18].value;
            count[19] += ptr_list[jump + 19].value;
            count[20] += ptr_list[jump + 20].value;
            count[21] += ptr_list[jump + 21].value;
            count[22] += ptr_list[jump + 22].value;
            count[23] += ptr_list[jump + 23].value;

            count[24] += ptr_list[jump + 24].value;
            count[25] += ptr_list[jump + 25].value;
            count[26] += ptr_list[jump + 26].value;
            count[27] += ptr_list[jump + 27].value;
            count[28] += ptr_list[jump + 28].value;
            count[29] += ptr_list[jump + 29].value;
            count[30] += ptr_list[jump + 30].value;
            count[31] += ptr_list[jump + 31].value;
        }
    }

    free(ptr_list);

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    return 0;
}