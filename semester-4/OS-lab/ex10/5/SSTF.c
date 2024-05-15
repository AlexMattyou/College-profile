#include <stdio.h>
#include <stdlib.h>

void sstf(int requests[], int n, int head) {
    int seek_count = 0;
    int distance, cur_track;
    int processed[n];
    int min_distance, min_index;
    for (int i = 0; i < n; i++) {
        processed[i] = 0;
    }
    printf("SSTF Disk Scheduling:\n");
    printf("Sequence of requests:\n");
    for (int i = 0; i < n; i++) {
        min_distance = __INT_MAX__;
        for (int j = 0; j < n; j++) {
            if (!processed[j]) {
                distance = abs(requests[j] - head);
                if (distance < min_distance) {
                    min_distance = distance;
                    min_index = j;
                }
            }
        }
        cur_track = requests[min_index];
        processed[min_index] = 1;
        printf("%d ", cur_track);
        seek_count += min_distance;
        head = cur_track;
    }
    printf("\nTotal seek operations: %d\n", seek_count);
}
int main() {
    int requests[] = {98, 183, 37, 122, 14, 124, 65, 67};
    int n = sizeof(requests) / sizeof(requests[0]);
    int head = 53;
    sstf(requests, n, head);
    return 0;
}
