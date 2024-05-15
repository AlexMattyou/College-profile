Creating a Pipe:

The pipe() system call is used to create a pipe. It takes an array of two integers (pipefd) as an argument. pipefd[0] is the read end, and pipefd[1] is the write end of the pipe.

Forking a Child Process:

The fork() system call is used to create a new process. It returns the process ID of the child process to the parent, and 0 to the child process.

Parent Process:

The parent process closes the read end of the pipe (pipefd[0]).
It writes a message to the write end of the pipe (pipefd[1]).
The parent process waits for the child process to complete using wait(NULL).

Child Process:

The child process closes the write end of the pipe (pipefd[1]).
It reads the message from the read end of the pipe (pipefd[0]) and prints it.