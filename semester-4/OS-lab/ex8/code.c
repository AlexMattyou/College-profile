#include <stdio.h>
#include <stdbool.h>
#define MAX_PROCESSES 5
#define MAX_RESOURCES 3
int available[MAX_RESOURCES];
int allocation[MAX_PROCESSES][MAX_RESOURCES];
int request[MAX_PROCESSES][MAX_RESOURCES];
bool deadlock_detection(int processes, int resources) {
    bool finish[MAX_PROCESSES] = {false};
    int work[MAX_RESOURCES];
    for (int i = 0; i < resources; i++) {
        work[i] = available[i];
    }
    bool found;
    do {
        found = false;
        for (int i = 0; i < processes; i++) {
            if (!finish[i]) {
                bool can_allocate = true;
                for (int j = 0; j < resources; j++) {
                    if (request[i][j] > work[j]) {
                        can_allocate = false;
                        break;
                    }
                }
                if (can_allocate) {
                    for (int j = 0; j < resources; j++) {
                        work[j] += allocation[i][j];
                    }
                    finish[i] = true;
                    found = true;
                }
            }
        }
    } while (found);
    for (int i = 0; i < processes; i++) {
        if (!finish[i]) {
            return true; // Deadlock detected
        }
    }
    return false;
}
int main() {
    int init_available[MAX_RESOURCES] = {3, 3, 2};
    int init_allocation[MAX_PROCESSES][MAX_RESOURCES] = {
        {0, 1, 0},
        {2, 0, 0},
        {3, 0, 2},
        {2, 1, 1},
        {0, 0, 2}
    };
    int init_request[MAX_PROCESSES][MAX_RESOURCES] = {
        {0, 0, 0},
        {2, 0, 2},
        {0, 0, 0},
        {1, 0, 0},
        {0, 0, 2}
    };
    for (int i = 0; i < MAX_RESOURCES; i++) {
        available[i] = init_available[i];
    }
    for (int i = 0; i < MAX_PROCESSES; i++) {
        for (int j = 0; j < MAX_RESOURCES; j++) {
            allocation[i][j] = init_allocation[i][j];
            request[i][j] = init_request[i][j];
        }
    }
    printf("Initial System State:\n");
    printf("Available Resources: ");
    for (int i = 0; i < MAX_RESOURCES; i++) {
        printf("%d ", available[i]);
    }
    printf("\n");
    printf("Allocation Matrix:\n");
    for (int i = 0; i < MAX_PROCESSES; i++) {
        for (int j = 0; j < MAX_RESOURCES; j++) {
            printf("%d ", allocation[i][j]);
        }
        printf("\n");
    }
    printf("Request Matrix:\n");
    for (int i = 0; i < MAX_PROCESSES; i++) {
        for (int j = 0; j < MAX_RESOURCES; j++) {
            printf("%d ", request[i][j]);
        }
        printf("\n");
    }
    if (deadlock_detection(MAX_PROCESSES, MAX_RESOURCES)) {
        printf("Deadlock detected in the system.\n");
    } else {
        printf("No deadlock in the system.\n");
    }
    return 0;
}




/*
OUTPUT:

Initial System State:
Available Resources: 3 3 2 
Allocation Matrix:
0 1 0 
2 0 0 
3 0 2 
2 1 1 
0 0 2 
Request Matrix:
0 0 0 
2 0 2 
0 0 0 
1 0 0 
0 0 2 
No deadlock in the system.

*/