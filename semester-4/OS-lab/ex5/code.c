#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    int pipefd[2];
    pid_t pid;
    char write_msg[] = "Hello from parent!";
    char read_msg[100];

    if (pipe(pipefd) == -1) {
        perror("pipe");
        return 1;
    }

    pid = fork();
    if (pid == -1) {
        perror("fork");
        return 1;
    }

    if (pid == 0) {
        close(pipefd[1]);
        read(pipefd[0], read_msg, sizeof(read_msg));
        printf("Child process received: %s\n", read_msg);
        close(pipefd[0]);
    } else {
        close(pipefd[0]);
        write(pipefd[1], write_msg, strlen(write_msg) + 1);
        printf("Parent process sent: %s\n", write_msg);
        close(pipefd[1]);
        wait(NULL);
    }
    return 0;
}

