#define _GNU_SOURCE

#include <stdint.h> /* for uint64_t */
#include <time.h>	/* for struct timespec */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sched.h>
#include <math.h>
#include <pthread.h>

#define LOOP_ITER 10000
#define LOOP_ITER_DOUBLE 10000.0

#define PERFORMANCE_OVERHEAD 34

//Minimal function call to ensure kernel thread has minimal functional overhead
void *function(void *args)
{
}

void main()
{
	const cpu_set_t cpuMask;
	sched_setaffinity(0, sizeof(cpu_set_t), &cpuMask);
	int i;
	unsigned int hi1, lo1, hi2, lo2;
	unsigned long begin;
	unsigned long end;
	double mean = 0;
	double variance = 0;
	double std_deviation = 0;
	unsigned long diff_array[LOOP_ITER];
	//Initialization for experiment specific code
	pthread_t thread;
	int pid;
	for (i = 0; i < LOOP_ITER; i++)
	{
		asm volatile("cpuid\n\t"
					 "rdtsc\n\t"
					 "mov %%edx, %0\n\t"
					 "mov %%eax, %1\n\t"
					 : "=r"(hi1), "=r"(lo1)::"%rax", "%rbx", "%rcx", "%rdx");
		pid = pthread_create(&thread, NULL, function, NULL);
		asm volatile("rdtscp\n\t"
					 "mov %%edx, %0\n\t"
					 "mov %%eax, %1\n\t"
					 "cpuid\n\t"
					 : "=r"(hi2), "=r"(lo2)::"%rax", "%rbx", "%rcx", "%rdx");
		begin = ((uint64_t)hi1 << 32) | lo1;
		end = ((uint64_t)hi2 << 32) | lo2;
		long result = (end - begin - PERFORMANCE_OVERHEAD);
		if (result < 0)
		{
			i--;
			continue;
		}
		diff_array[i] = result;
		pthread_cancel(thread);
	}
	for (i = 0; i < LOOP_ITER; i++)
	{
		mean += diff_array[i] / LOOP_ITER_DOUBLE;
	}
	for (i = 0; i < LOOP_ITER; i++)
	{
		variance += (pow((diff_array[i] - mean), 2)) / LOOP_ITER_DOUBLE;
	}
	std_deviation = sqrt(variance);
	printf("\nKernel Thread Overhead(Mean) : %lf", mean);
	printf("\nKernel Thread Overhead(Variance) : %lf", variance);
	printf("\nKernel Thread Overhead(Standard Deviation) : %lf\n", std_deviation);
}
