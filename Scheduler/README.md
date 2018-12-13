# Scheduler
The process scheduling is the activity of the process manager that handles the removal of the running process from the CPU and the selection of another process on the basis of a particular strategy. In this context, it is possible to determinate different time metrics.

| Metric            | Meaning                                                                                         |
|-------------------|-------------------------------------------------------------------------------------------------|
|Arrival Time       |Time at which the process arrives in the ready queue.                                            |
|Burst Time         |Time required by a process for CPU execution.                                                    |
|Turnaround Time    |Time taken between the submission of process for execution and the return of the complete output.|  
|Response Time      |Time between when the process is submitted and the first response is produced.                   |
|Waiting Time       |Time the process has waited in the waiting queue.                                                |

Write a program that given a list of processes calculates the average turnaround, response and waiting time with three different algorithms (first in first served, shortest job first, round robin with quantum of 2). 

## Input
The input file consist of a series of lines, each line containing a pair of integers giving the arrival time and burst time of a process. 

## Output
For each algorithm print a new line with the algorithm's initials followed by the average turnaround, response and waiting time with one digit after the decimal point.

| Input Sample             | Output Sample                                                |
|--------------------------|--------------------------------------------------------------|
|0 20<br>0 10<br>4 6<br>4 8| FCFS 30.5 19.5 19.5<br>SJF 21.5 10.5 10.5<br>RR 31.5 2.0 20.5|