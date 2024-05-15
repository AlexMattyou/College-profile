#include <stdio.h>
#include <limits.h>

void fcfs(int n, int bt[]);
void sjf(int n, int bt[]);
void srtf(int n, int bt[]);
void priority_scheduling(int n, int bt[], int prio[]);

int main() {
    int n = 5;
    int bt[] = {10, 5, 8, 6, 2};
    int prio[] = {3, 1, 4, 5, 2};

    printf("First-Come, First-Served (FCFS):\n");
    fcfs(n, bt);

    printf("\nShortest Job First (SJF):\n");
    sjf(n, bt);

    printf("\nShortest Remaining Time First (SRTF):\n");
    srtf(n, bt);

    printf("\nPriority Scheduling:\n");
    priority_scheduling(n, bt, prio);

    return 0;
}

void fcfs(int n, int bt[]) {
    int wt[20], tat[20];
    int total_wt = 0, total_tat = 0;

    wt[0] = 0;
    for (int i = 1; i < n; i++) {
        wt[i] = wt[i - 1] + bt[i - 1];
    }

    printf("Process\tBurst_Time\tWaiting_Time\tTurnaround_Time\n");
    for (int i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];
        total_wt += wt[i];
        total_tat += tat[i];
        printf("P[%d]\t%d\t\t%d\t\t%d\n", i + 1, bt[i], wt[i], tat[i]);
    }

    printf("Average waiting time = %.2f\n", (float)total_wt / n);
    printf("Average turnaround time = %.2f\n", (float)total_tat / n);
}

void sjf(int n, int bt[]) {
    int wt[20], tat[20];
    int total_wt = 0, total_tat = 0;
    int temp, i, j;

    int sorted_bt[20];
    for (i = 0; i < n; i++) {
        sorted_bt[i] = bt[i];
    }

    // Sort Burst_Times
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (sorted_bt[i] > sorted_bt[j]) {
                temp = sorted_bt[i];
                sorted_bt[i] = sorted_bt[j];
                sorted_bt[j] = temp;
            }
        }
    }

    wt[0] = 0;
    for (i = 1; i < n; i++) {
        wt[i] = wt[i - 1] + sorted_bt[i - 1];
    }

    printf("Process\tBurst_Time\tWaiting_Time\tTurnaround_Time\n");
    for (i = 0; i < n; i++) {
        tat[i] = sorted_bt[i] + wt[i];
        total_wt += wt[i];
        total_tat += tat[i];
        printf("P[%d]\t%d\t\t%d\t\t%d\n", i + 1, sorted_bt[i], wt[i], tat[i]);
    }

    printf("Average waiting time = %.2f\n", (float)total_wt / n);
    printf("Average turnaround time = %.2f\n", (float)total_tat / n);
}

void srtf(int n, int bt[]) {
    int rt[20], wt[20] = {0}, tat[20];
    int total_wt = 0, total_tat = 0;
    int complete = 0, t = 0, minm = INT_MAX;
    int shortest = 0, finish_time;
    int check = 0;

    for (int i = 0; i < n; i++) {
        rt[i] = bt[i];
    }

    while (complete != n) {
        for (int j = 0; j < n; j++) {
            if ((rt[j] < minm) && (rt[j] > 0)) {
                minm = rt[j];
                shortest = j;
                check = 1;
            }
        }

        if (check == 0) {
            t++;
            continue;
        }

        rt[shortest]--;
        minm = rt[shortest];
        if (minm == 0) minm = INT_MAX;

        if (rt[shortest] == 0) {
            complete++;
            check = 0;
            finish_time = t + 1;
            wt[shortest] = finish_time - bt[shortest] - wt[shortest];

            if (wt[shortest] < 0) wt[shortest] = 0;
        }

        t++;
    }

    for (int i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];
        total_wt += wt[i];
        total_tat += tat[i];
    }

    printf("Process\tBurst_Time\tWaiting_Time\tTurnaround_Time\n");
    for (int i = 0; i < n; i++) {
        printf("P[%d]\t%d\t\t%d\t\t%d\n", i + 1, bt[i], wt[i], tat[i]);
    }

    printf("Average waiting time = %.2f\n", (float)total_wt / n);
    printf("Average turnaround time = %.2f\n", (float)total_tat / n);
}

void priority_scheduling(int n, int bt[], int prio[]) {
    int wt[20], tat[20];
    int total_wt = 0, total_tat = 0;
    int i, j, temp;

    int sorted_bt[20], sorted_prio[20];
    for (i = 0; i < n; i++) {
        sorted_bt[i] = bt[i];
        sorted_prio[i] = prio[i];
    }

    // Sort based on priority
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (sorted_prio[i] > sorted_prio[j]) {
                temp = sorted_prio[i];
                sorted_prio[i] = sorted_prio[j];
                sorted_prio[j] = temp;

                temp = sorted_bt[i];
                sorted_bt[i] = sorted_bt[j];
                sorted_bt[j] = temp;
            }
        }
    }

    wt[0] = 0;
    for (i = 1; i < n; i++) {
        wt[i] = wt[i - 1] + sorted_bt[i - 1];
    }

    printf("Process\tBurst_Time\tPriority\tWaiting_Time\tTurnaround_Time\n");
    for (i = 0; i < n; i++) {
        tat[i] = sorted_bt[i] + wt[i];
        total_wt += wt[i];
        total_tat += tat[i];
        printf("P[%d]\t%d\t\t%d\t\t%d\t\t%d\n", i + 1, sorted_bt[i], sorted_prio[i], wt[i], tat[i]);
    }

    printf("Average waiting time = %.2f\n", (float)total_wt / n);
    printf("Average turnaround time = %.2f\n", (float)total_tat / n);
}
