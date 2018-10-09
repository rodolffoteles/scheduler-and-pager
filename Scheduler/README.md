# Scheduler
The process scheduling is the activity of the process manager that handles the removal of the running process from the CPU and the selection of another process on the basis of a particular strategy. Here you have to calculate some metrics 

## Input
The input file consist of a series of lines, each line containing a pair of integers giving the arrival time and burst time of a process. 

## Output
For each algorithm print a new line with the algorithm's initials followed by the average turnaround, response and waiting time with one digit after the decimal point.

| Input Sample             | Output Sample                                                |
|--------------------------|--------------------------------------------------------------|
|0 20<br>0 10<br>4 6<br>4 8| FCFS 30.5 19.5 19.5<br>SJF 21.5 10.5 10.5<br>RR 31.5 2.0 20.5|