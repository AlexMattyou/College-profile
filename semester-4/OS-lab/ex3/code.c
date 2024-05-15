#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>

int main() {
    pid_t child_pid, parent_pid;

    parent_pid = getpid();
    printf("Parent process PID: %d\n", parent_pid);

    child_pid = fork();

    if (child_pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (child_pid == 0) {
        pid_t child_pid = getpid();
        printf("Child process PID: %d\n", child_pid);

        execl("/bin/ls", "ls", "-l", NULL);

        perror("execl");
        exit(EXIT_FAILURE);
    } else {
        close(STDOUT_FILENO);

        wait(NULL);

        printf("Child process terminated.\n");

        exit(EXIT_SUCCESS);
    }

    return 0;
}

