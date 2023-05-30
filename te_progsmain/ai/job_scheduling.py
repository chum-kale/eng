def job_scheduler(job_info, t):
    scheduled_jobs = []
    n = len(job_info)
    for i in range(n):
        for j in range(n - 1 - i):
            if job_info[j][2] < job_info[j + 1][2]:
                job_info[j], job_info[j + 1] = job_info[j + 1], job_info[j]

    total_time = 0
    max_profit = 0
    max = t

    for i in range(n):
       if job_info[i][1] < max:
           max = max - job_info[i][1]
           scheduled_jobs.append(job_info[i][0])
           total_time = total_time + job_info[i][1]
           max_profit = max_profit + job_info[i][2]

    print(scheduled_jobs)
    print ("MAx profit achieved is {0}".format(max_profit))
    print ("Time achieved is {0}".format(total_time))

if __name__ == '__main__':
    arr = [['a', 2, 100],  
              ['b', 1, 19],
              ['c', 2, 27],
              ['d', 1, 25],
              ['e', 3, 15]]
    
    x = int(input("Enter time available:"))
    print("Best possible solution is: ")
    job_scheduler(arr, x+1)


    