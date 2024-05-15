#include <stdio.h>
#include <stdbool.h>
#define MAX_PROCESSES 5
#define MAX_RESOURCES 3
int available[MAX_RESOURCES];
int maximum[MAX_PROCESSES][MAX_RESOURCES];
int allocation[MAX_PROCESSES][MAX_RESOURCES];
int need[MAX_PROCESSES][MAX_RESOURCES];

void calculate_need() {
    for (int i = 0; i < MAX_PROCESSES; i++) {
        for (int j = 0; j < MAX_RESOURCES; j++) {
            need[i][j] = maximum[i][j] - allocation[i][j];
        }
    }
}

bool is_safe() {
    bool finish[MAX_PROCESSES] = {false};
    int work[MAX_RESOURCES];
    for (int i = 0; i < MAX_RESOURCES; i++) {
        work[i] = available[i];
    }

    while (true) {
        bool found = false;
        for (int i = 0; i < MAX_PROCESSES; i++) {
            if (!finish[i]) {
                bool can_allocate = true;
                for (int j = 0; j < MAX_RESOURCES; j++) {
                    if (need[i][j] > work[j]) {
                        can_allocate = false;
                        break;
                    }
                }
                if (can_allocate) {
                    for (int j = 0; j < MAX_RESOURCES; j++) {
                        work[j] += allocation[i][j];
                    }
                    finish[i] = true;
                    found = true;
                }
            }
        }
        if (!found) {
            break;
        }
    }
    for (int i = 0; i < MAX_PROCESSES; i++) {
        if (!finish[i]) {
            return false;
        }
    }
    return true;
}
bool request_resources(int process_num, int request[]) {
    for (int i = 0; i < MAX_RESOURCES; i++) {
        if (request[i] > need[process_num][i]) {
            printf("Error: Process has exceeded its maximum claim.\n");
            return false;
        }
    }
    for (int i = 0; i < MAX_RESOURCES; i++) {
        if (request[i] > available[i]) {
            printf("Error: Resources are not available.\n");
            return false;
        }
    }
    for (int i = 0; i < MAX_RESOURCES; i++) {
        available[i] -= request[i];
        allocation[process_num][i] += request[i];
        need[process_num][i] -= request[i];
    }
    if (is_safe()) {
        return true;
    } else {
        for (int i = 0; i < MAX_RESOURCES; i++) {
            available[i] += request[i];
            allocation[process_num][i] -= request[i];
            need[process_num][i] += request[i];
        }
        printf("Error: Request would lead to an unsafe state.\n");
        return false;
    }
}

void release_resources(int process_num, int release[]) {
    for (int i = 0; i < MAX_RESOURCES; i++) {
        available[i] += release[i];
        allocation[process_num][i] -= release[i];
        need[process_num][i] += release[i];
    }
}

int main() {
    int init_available[MAX_RESOURCES] = {3, 3, 2};
    int init_maximum[MAX_PROCESSES][MAX_RESOURCES] = {
        {7, 5, 3},
        {3, 2, 2},
        {9, 0, 2},
        {2, 2, 2},
        {4, 3, 3}
    };
    int init_allocation[MAX_PROCESSES][MAX_RESOURCES] = {
        {0, 1, 0},
        {2, 0, 0},
        {3, 0, 2},
        {2, 1, 1},
        {0, 0, 2}
    };
    for (int i = 0; i < MAX_RESOURCES; i++) {
        available[i] = init_available[i];
    }
    for (int i = 0; i < MAX_PROCESSES; i++) {
        for (int j = 0; j < MAX_RESOURCES; j++) {
            maximum[i][j] = init_maximum[i][j];
            allocation[i][j] = init_allocation[i][j];
        }
    }
    calculate_need();
    printf("Initial System State:\n");
    printf("Available Resources: ");
    for (int i = 0; i < MAX_RESOURCES; i++) {
        printf("%d ", available[i]);
    }
    printf("\n");
    printf("Maximum Resources:\n");
    for (int i = 0; i < MAX_PROCESSES; i++) {
        for (int j = 0; j < MAX_RESOURCES; j++) {
            printf("%d ", maximum[i][j]);
        }
        printf("\n");
    }
    printf("Allocated Resources:\n");
    for (int i = 0; i < MAX_PROCESSES; i++) {
        for (int j = 0; j < MAX_RESOURCES; j++) {
            printf("%d ", allocation[i][j]);
        }
        printf("\n");
    }
    int request1[MAX_RESOURCES] = {1, 0, 2};
    printf("Process P1 requesting resources: {1, 0, 2}\n");
    if (request_resources(1, request1)) {
        printf("Request approved.\n");
    }
    printf("Current Available Resources: ");
    for (int i = 0; i < MAX_RESOURCES; i++) {
        printf("%d ", available[i]);
    }
    printf("\n");
    int release1[MAX_RESOURCES] = {1, 0, 2};
    printf("Process P1 releasing resources: {1, 0, 2}\n");
    release_resources(1, release1);
    printf("Current Available Resources: ");
    for (int i = 0; i < MAX_RESOURCES; i++) {
        printf("%d ", available[i]);
    }
    printf("\n");
    return 0;
}
