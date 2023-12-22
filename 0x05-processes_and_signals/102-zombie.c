#include <unistd.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>

/**
 * infinite_while - infinite while loop
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * create_zombie_process - a function that create sombie process
 * @count: num of process to create
 */
void create_zombie_process(size_t count)
{
	size_t i = 0;
	pid_t pid;

	while (i < count)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			i++;
		}
		else if (pid == 0)
			exit(EXIT_SUCCESS);
	}
}
/**
 * main - Entry point
 * Return: always zero
 */
int main(void)
{
	create_zombie_process(5);
	infinite_while();
	exit(EXIT_SUCCESS);
}
