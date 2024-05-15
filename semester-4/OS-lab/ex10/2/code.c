#include <stdio.h>
#include <stdbool.h>
#define NUM_FRAMES 3
#define NUM_PAGES 7
void fifo(int pages[], int num_pages) {
    int frames[NUM_FRAMES] = {-1};
    int frame_index = 0;
    int page_faults = 0;
    printf("Page Replacement using FIFO:\n");
    for (int i = 0; i < num_pages; i++) {
        int page = pages[i];
        bool page_found = false;
        for (int j = 0; j < NUM_FRAMES; j++) {
            if (frames[j] == page) {
                page_found = true;
                break;
            }
        }
        if (!page_found) {
            frames[frame_index] = page;
            frame_index = (frame_index + 1) % NUM_FRAMES;
            page_faults++;
        }
        printf("Page %d: ", page);
        for (int j = 0; j < NUM_FRAMES; j++) {
            if (frames[j] == -1) {
                printf("- ");
            } else {
                printf("%d ", frames[j]);
            }
        }
        printf("\n");
    }
    printf("Total Page Faults: %d\n", page_faults);
}
int main() {
    int pages[NUM_PAGES] = {1, 2, 3, 4, 1, 5, 6};
    fifo(pages, NUM_PAGES);
    return 0;
}
