Data Structures:

available[]: Keeps track of the available instances of each resource.
maximum[][]: The maximum demand of each process.
allocation[][]: The amount currently allocated to each process.
need[][]: The remaining needs of each process, calculated as maximum - allocation.

Functions:

calculate_need(): Calculates the remaining needs of each process.
is_safe(): Checks if the system is in a safe state.
request_resources(process_num, request[]): Attempts to allocate requested resources to a process if it leaves the system in a safe state.
release_resources(process_num, release[]): Releases resources from a process.

Main Function:

Initializes the system state.
Demonstrates a resource request and release scenario.