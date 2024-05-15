#include <stdio.h>

#define MAX_MEMORY_SIZE 100

void best_fit(int memory[], int num_processes, int process_sizes[]) {
    int i, j, min_index;
    for (i = 0; i < num_processes; i++) {
        min_index = -1;
        for (j = 0; j < MAX_MEMORY_SIZE; j++) {
            if (memory[j] >= process_sizes[i]) {
                if (min_index == -1 || memory[j] < memory[min_index]) {
                    min_index = j;
                }
            }
        }
        if (min_index != -1) {
            memory[min_index] -= process_sizes[i];
            printf("Process %d allocated at memory location %d\n", i+1, min_index);
        } else {
            printf("Process %d cannot be allocated\n", i+1);
        }
    }
}

int main() {
    int memory[MAX_MEMORY_SIZE] = {100};
    int num_processes = 3;
    int process_sizes[] = {30, 20, 10};

    printf("Best Fit Memory Allocation:\n");
    best_fit(memory, num_processes, process_sizes);

    return 0;
}

