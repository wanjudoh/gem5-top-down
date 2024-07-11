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
        srand((unsigned int)time(NULL));
        for (int j = 0; j <= size - 32; j += 32) {
            int index = (rand() % (size / 32)) * 32;
            
            count += ptr_list[index].value;
            count += ptr_list[index + 1].value;
            count += ptr_list[index + 2].value;
            count += ptr_list[index + 3].value;
            count += ptr_list[index + 4].value;
            count += ptr_list[index + 5].value;
            count += ptr_list[index + 6].value;
            count += ptr_list[index + 7].value;

            count += ptr_list[index + 8].value;
            count += ptr_list[index + 9].value;
            count += ptr_list[index + 10].value;
            count += ptr_list[index + 11].value;
            count += ptr_list[index + 12].value;
            count += ptr_list[index + 13].value;
            count += ptr_list[index + 14].value;
            count += ptr_list[index + 15].value;

            count += ptr_list[index + 16].value;
            count += ptr_list[index + 17].value;
            count += ptr_list[index + 18].value;
            count += ptr_list[index + 19].value;
            count += ptr_list[index + 20].value;
            count += ptr_list[index + 21].value;
            count += ptr_list[index + 22].value;
            count += ptr_list[index + 23].value;

            count += ptr_list[index + 24].value;
            count += ptr_list[index + 25].value;
            count += ptr_list[index + 26].value;
            count += ptr_list[index + 27].value;
            count += ptr_list[index + 28].value;
            count += ptr_list[index + 29].value;
            count += ptr_list[index + 30].value;
            count += ptr_list[index + 31].value;
        }
    }

    free(ptr_list);

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    return 0;
}