#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define NUM_THREADS 5

sem_t semaphore;

void* thread_function(void* arg) {
    int thread_num = *((int*)arg);
    printf("Thread %d waiting to enter critical section...\n", thread_num);
    sem_wait(&semaphore); // P operation (wait)
    printf("Thread %d entered critical section.\n", thread_num);
    sleep(1);
    printf("Thread %d leaving critical section.\n", thread_num);
    sem_post(&semaphore); // V operation (signal)
    free(arg);
    return NULL;
}

int main() {
    pthread_t threads[NUM_THREADS];

    if (sem_init(&semaphore, 0, 1) != 0) {
        perror("sem_init");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        int* thread_num = (int*)malloc(sizeof(int));
        if (thread_num == NULL) {
            perror("malloc");
            exit(EXIT_FAILURE);
        }
        *thread_num = i + 1;
        if (pthread_create(&threads[i], NULL, thread_function, thread_num) != 0) {
            perror("pthread_create");
            free(thread_num);  // Free memory if thread creation fails
            exit(EXIT_FAILURE);
        }
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    sem_destroy(&semaphore);
    return 0;
}



/*
OUTPUT:

Thread 1 waiting to enter critical section...
Thread 1 entered critical section.
Thread 2 waiting to enter critical section...
Thread 3 waiting to enter critical section...
Thread 4 waiting to enter critical section...
Thread 5 waiting to enter critical section...
Thread 1 leaving critical section.
Thread 2 entered critical section.
Thread 2 leaving critical section.
Thread 3 entered critical section.
Thread 3 leaving critical section.
Thread 4 entered critical section.
Thread 4 leaving critical section.
Thread 5 entered critical section.
Thread 5 leaving critical section.

*/
