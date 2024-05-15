First Fit Memory Allocation:

Iterate through each process.
For each process, iterate through memory blocks and allocate it to the first block that has enough space.
If no suitable block is found, declare allocation failure.

Worst Fit Memory Allocation:

Iterate through each process.
For each process, find the largest memory block that can accommodate it.
Allocate the process to this block. If no suitable block is found, declare allocation failure.

Best Fit Memory Allocation:

Iterate through each process.
For each process, find the smallest memory block that can accommodate it.
Allocate the process to this block. If no suitable block is found, declare allocation failure.