#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
void main(int argc, char *argv[])
{
	int pid;
	pid = fork();
	if (pid==0){/*fork returns 0 if in child process*/
		printf("The child process's pid is %d\n", getpid());
	}
	exit(0);
}
