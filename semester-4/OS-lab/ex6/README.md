Semaphore Initialization:

The sem_init() function initializes the semaphore. The second argument (0) indicates that the semaphore is shared between threads of a process (not between processes). The third argument (1) sets the initial value of the semaphore to 1, making it a binary semaphore.

Thread Creation:

Five threads are created. Each thread runs the thread_function(), which attempts to enter the critical section.

Critical Section:

sem_wait(&semaphore) decreases the semaphore value by 1. If the semaphore value is greater than 0, the thread enters the critical section. If the semaphore value is 0, the thread blocks until the semaphore value becomes positive.
Inside the critical section, the thread prints its number and simulates some work by sleeping for 1 second.
sem_post(&semaphore) increases the semaphore value by 1, allowing other threads to enter the critical section.

Semaphore Destruction:

After all threads have finished execution, the semaphore is destroyed using sem_destroy().