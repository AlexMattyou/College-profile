Data Structures:

available[]: Keeps track of the available instances of each resource.
allocation[][]: The amount currently allocated to each process.
request[][]: The current resource requests of each process.

Deadlock Detection Function:

deadlock_detection(): This function checks for deadlock by simulating the allocation of resources and ensuring that all processes can eventually complete.
Main Function:

Initializes the system state.
Displays the current state of available resources, allocation matrix, and request matrix.
Calls the deadlock detection function and prints whether a deadlock is detected or not.

Example Use Case:
The example initializes the system with 5 processes and 3 resources. It then checks if there is a deadlock with the current allocation and request states.

You can modify the init_available, init_allocation, and init_request arrays to simulate different scenarios and see how the algorithm performs in detecting deadlocks.