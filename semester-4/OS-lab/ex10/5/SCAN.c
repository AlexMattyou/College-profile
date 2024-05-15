#include <stdio.h>
#include <stdlib.h>

void scan(int requests[], int n, int head, int direction) {
    int seek_count = 0;
    int distance, cur_track;
    int size = 200;
    int left[n], right[n];
    int left_count = 0, right_count = 0;

    if (direction == -1) {
        left[left_count++] = 0;
    } else {
        right[right_count++] = size - 1;
    }

    for (int i = 0; i < n; i++) {
        if (requests[i] < head) {
            left[left_count++] = requests[i];
        } else {
            right[right_count++] = requests[i];
        }
    }

    qsort(left, left_count, sizeof(int), cmpfunc);
    qsort(right, right_count, sizeof(int), cmpfunc);

    printf("SCAN Disk Scheduling:\n");
    printf("Sequence of requests:\n");

    int run[] = (direction == -1) ? left : right;
    int run_count = (direction == -1) ? left_count : right_count;

    for (int i = 0; i < run_count; i++) {
        cur_track = run[i];
        printf("%d ", cur_track);

        distance = abs(cur_track - head);
        seek_count += distance;

        head = cur_track;
    }

    printf("\nTotal seek operations: %d\n", seek_count);
}

int cmpfunc(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    int requests[] = {98, 183, 37, 122, 14, 124, 65, 67};
    int n = sizeof(requests) / sizeof(requests[0]);
    int head = 53;
    int direction = 1; // 1 for right, -1 for left

    scan(requests, n, head, direction);

    return 0;
}
