#include <iostream>
#include <string>

using namespace std;

struct list {
    struct list *next_element;
    char pad[22];
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
    element *ptr_this;

    ptr_this = ptr_list;
    for (int i = 0; i < size; i++) {
        ptr_this->next_element = &ptr_list[i + 1];
        ptr_this = ptr_this->next_element;
        ptr_this->next_element = nullptr;
    }

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    ptr_this = ptr_list;
    for (int i = 0; i < iterations; i++) {
        ptr_this = ptr_list;
        for (int j = 0; j <= size - 32; j += 32) {
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;

            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;

            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;

            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;
            ptr_this = ptr_this->next_element;            
        }
    }

    free(ptr_list);

    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");
    __asm__ __volatile__("nop");

    return 0;
}