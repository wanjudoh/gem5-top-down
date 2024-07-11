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

    element *ptr_list = nullptr;
    ptr_list = (element *)aligned_alloc(32, sizeof(element) * size);

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    for (int i = 0; i < iterations; i++) {
        for (int j = 0; j <= size - 32; j += 32) {
            ptr_list[j].value = j;
            ptr_list[j + 1].value = j;
            ptr_list[j + 2].value = j;
            ptr_list[j + 3].value = j;
            ptr_list[j + 4].value = j;
            ptr_list[j + 5].value = j;
            ptr_list[j + 6].value = j;
            ptr_list[j + 7].value = j;

            ptr_list[j + 8].value = j;
            ptr_list[j + 9].value = j;
            ptr_list[j + 10].value = j;
            ptr_list[j + 11].value = j;
            ptr_list[j + 12].value = j;
            ptr_list[j + 13].value = j;
            ptr_list[j + 14].value = j;
            ptr_list[j + 15].value = j;

            ptr_list[j + 16].value = j;
            ptr_list[j + 17].value = j;
            ptr_list[j + 18].value = j;
            ptr_list[j + 19].value = j;
            ptr_list[j + 20].value = j;
            ptr_list[j + 21].value = j;
            ptr_list[j + 22].value = j;
            ptr_list[j + 23].value = j;
            
            ptr_list[j + 24].value = j;
            ptr_list[j + 25].value = j;
            ptr_list[j + 26].value = j;
            ptr_list[j + 27].value = j;
            ptr_list[j + 28].value = j;
            ptr_list[j + 29].value = j;
            ptr_list[j + 30].value = j;
            ptr_list[j + 31].value = j;
        }
    }

    free(ptr_list);

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    return 0;
}