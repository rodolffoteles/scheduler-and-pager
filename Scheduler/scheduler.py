import sys

def read_jobs_from_file(file_name):
    jobs = []
    with open(file_name) as file:
        for line in file:
            jobs.append([int(t) for t in line.split()])
    jobs.sort(key=lambda j: j[0])
    return jobs

def first_come_first_served(jobs):
    jobs = jobs[:]
    turnaround = response = waiting = 0
    time = jobs[0][0]
    job_count = len(jobs)

    while jobs:
        job = jobs.pop(0)
        response += time - job[0]
        waiting += time - job[0]
        time += job[1]
        turnaround += time - job[0]

    return [round(t/job_count, 1) for t in [turnaround, response, waiting]]

def shortest_job_first(jobs):
    jobs = jobs[:]
    turnaround = response = waiting = 0
    time = jobs[0][0]
    job_count = len(jobs)

    while jobs:
        try:
            job = min([j for j in jobs if j[0] <= time], key=lambda j: j[1])
            jobs.remove(job)
        except ValueError:
            time = jobs[0][0]
            continue
        
        response += time - job[0]
        waiting += time - job[0]
        time += job[1]
        turnaround += time - job[0]

    return [round(t/job_count, 1) for t in [turnaround, response, waiting]]

def round_robin(jobs, quantum=2):
    jobs = jobs[:]
    turnaround = response = waiting = 0
    time = jobs[0][0]
    job_count = len(jobs)

    while jobs:
        try:
            job = [j for j in jobs if j[0] <= time][0]
            jobs.remove(job)
        except IndexError:
            time = jobs[0][0]
            continue
            
        if len(job) == 2:
            response += time - job[0]
            job.append(job[0])  

        waiting += time - job[0]
        time += quantum if job[1] > quantum else job[1]
        job[1] -= quantum
        job[0] = time

        if job[1] > 0: 
            jobs.append(job)
            jobs.sort(key=lambda j: j[0])
        else:
            turnaround += time - job[2]

    return [round(t/job_count, 1) for t in [turnaround, response, waiting]]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python scheduler.py <processes_file>.txt')
        exit(1)

    jobs = read_jobs_from_file(sys.argv[1])
    print('FCRS {}'.format(
        ' '.join([str(t) for t in first_come_first_served(jobs)])
        ))

    print('SJF {}'.format(
        ' '.join([str(t) for t in shortest_job_first(jobs)])
        ))

    print('RR {}'.format(
        ' '.join([str(t) for t in round_robin(jobs)])
        ))   