#include <stdio.h>

#define MAX_MEMORY_SIZE 100

void first_fit(int memory[], int num_processes, int process_sizes[]) {
    int i, j;
    for (i = 0; i < num_processes; i++) {
        for (j = 0; j < MAX_MEMORY_SIZE; j++) {
            if (memory[j] >= process_sizes[i]) {
                memory[j] -= process_sizes[i];
                printf("Process %d allocated at memory location %d\n", i+1, j);
                break;
            }
        }
        if (j == MAX_MEMORY_SIZE) {
            printf("Process %d cannot be allocated\n", i+1);
        }
    }
}

int main() {
    int memory[MAX_MEMORY_SIZE] = {100};
    int num_processes = 3;
    int process_sizes[] = {30, 20, 10};

    printf("First Fit Memory Allocation:\n");
    first_fit(memory, num_processes, process_sizes);

    return 0;
}

