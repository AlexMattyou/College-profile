FCFS (First-Come-First-Serve) Disk Scheduling:
Initialize: Set the starting head position.
Process Requests: Iterate through the requests in order, calculating the seek distance for each.
Output: Print the order of requests and total seek operations.

SSTF (Shortest Seek Time First) Disk Scheduling:
Initialize: Set the starting head position and mark all requests as unprocessed.
Find Nearest Request: For each request, find the unprocessed request closest to the current head position.
Process Requests: Move to the closest request, mark it as processed, and update the seek count.
Output: Print the order of requests and total seek operations.

SCAN (Elevator) Disk Scheduling:
Initialize: Set the starting head position and direction (left or right).
Separate Requests: Divide requests into those on the left and right of the head.
Sort Requests: Sort requests on both sides.
Process Requests: Move in the specified direction, processing all requests until reaching the end, then reverse direction if necessary.