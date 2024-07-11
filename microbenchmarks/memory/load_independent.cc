#include <iostream>
#include <string>

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

    int count = 0;
    element *ptr_list = nullptr;
    ptr_list = (element *)aligned_alloc(32, sizeof(element) * size);

    for (int i = 0; i < size; i++) {
        ptr_list[i].value = 1;
    }

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    for (int i = 0; i < iterations; i++) {
        for (int j = 0; j <= size - 32; j += 32) {
            count += ptr_list[j].value;
            count += ptr_list[j + 1].value;
            count += ptr_list[j + 2].value;
            count += ptr_list[j + 3].value;
            count += ptr_list[j + 4].value;
            count += ptr_list[j + 5].value;
            count += ptr_list[j + 6].value;
            count += ptr_list[j + 7].value;

            count += ptr_list[j + 8].value;
            count += ptr_list[j + 9].value;
            count += ptr_list[j + 10].value;
            count += ptr_list[j + 11].value;
            count += ptr_list[j + 12].value;
            count += ptr_list[j + 13].value;
            count += ptr_list[j + 14].value;
            count += ptr_list[j + 15].value;

            count += ptr_list[j + 16].value;
            count += ptr_list[j + 17].value;
            count += ptr_list[j + 18].value;
            count += ptr_list[j + 19].value;
            count += ptr_list[j + 20].value;
            count += ptr_list[j + 21].value;
            count += ptr_list[j + 22].value;
            count += ptr_list[j + 23].value;

            count += ptr_list[j + 24].value;
            count += ptr_list[j + 25].value;
            count += ptr_list[j + 26].value;
            count += ptr_list[j + 27].value;
            count += ptr_list[j + 28].value;
            count += ptr_list[j + 29].value;
            count += ptr_list[j + 30].value;
            count += ptr_list[j + 31].value;
        }
    }

    free(ptr_list);

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    return 0;
}