Initialize Frames:

Initialize an array frames with NUM_FRAMES elements set to -1 to represent empty frames.
Initialize frame_index to 0 for tracking the oldest frame and page_faults to 0 for counting page faults.
Process Each Page:

For each page in the reference string pages[]:
Check if the page is already in the frames.
If the page is not found in the frames:
Replace the page at frame_index with the new page.
Update frame_index to point to the next frame in a circular manner.
Increment the page fault counter.
Print Frames State:

After processing each page, print the current state of the frames.
Print Total Page Faults:

After processing all pages, print the total number of page faults.