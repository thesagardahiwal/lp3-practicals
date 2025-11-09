class Job:
    def __init__ (self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit
    
def job_sequencing(jobs):
    jobs.sort(key = lambda x : x.profit, reverse = True)
    max_deadline = max(job.deadline for job in jobs)
    result = [-1] * max_deadline
    slot = [False] * max_deadline
    
    total_profit = 0
    scheduled_jobs = []
    
    for job in jobs:
        for j in range(min(max_deadline - 1, job.deadline - 1), -1, -1):
            if not slot[j]:
                result[j] = job.id
                slot[j] =True
                scheduled_jobs.append(job.id)
                total_profit += job.profit
                break
    
    return scheduled_jobs, total_profit

def main():
    jobs = [
        Job('a', 2, 100),
        Job('b', 1, 19),
        Job('c', 2, 27),
        Job('d', 1, 25),
        Job('e', 3, 15)
    ]
    
    scheduled_jobs, total_profit = job_sequencing(jobs)
    print("Scheduled Jobs:", scheduled_jobs)
    print("Total Profit:", total_profit)

if __name__ == "__main__":    
    main()