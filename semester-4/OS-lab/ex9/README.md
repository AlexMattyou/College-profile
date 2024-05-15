pthread_create: This function creates a new thread. It takes four arguments: a pointer to the thread variable, thread attributes (can be NULL for default attributes), a pointer to the function to be executed by the thread, and arguments to pass to the function.

pthread_join: This function waits for the thread specified by thread to terminate. It takes two arguments: the thread variable and a pointer to a location to store the exit status of the thread (can be NULL if not required).

pthread_exit: This function is used to exit a thread. It takes a single argument that is passed back to the thread's joiner as the thread's exit status.