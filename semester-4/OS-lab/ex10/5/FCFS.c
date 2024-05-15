#include <stdio.h>

void fcfs(int requests[], int n, int head) {
    int seek_count = 0;
    int distance, cur_track;

    printf("FCFS Disk Scheduling:\n");
    printf("Sequence of requests:\n");

    for (int i = 0; i < n; i++) {
        cur_track = requests[i];
        printf("%d ", cur_track);

        distance = abs(cur_track - head);
        seek_count += distance;

        head = cur_track;
    }
    printf("\nTotal seek operations: %d\n", seek_count);
}

int main() {
    int requests[] = {98, 183, 37, 122, 14, 124, 65, 67};
    int n = sizeof(requests) / sizeof(requests[0]);
    int head = 53;

    fcfs(requests, n, head);

    return 0;
}
