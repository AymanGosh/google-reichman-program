import heapq
import random


# Function to simulate the job scheduling without using a class
def simulate_scheduler(initial_jobs_data):
    # Priority queue (min-heap) - elements are tuples
    # (-priority, arrival_time, job_id, name, duration, remaining_time, start_time)
    current_time = 0
    job_queue = []
    completed_jobs = []
    job_counter = 1
    current_job = None

    # Push initial jobs
    for name, priority, duration in initial_jobs_data:
        heapq.heappush(job_queue, (-priority, 0, job_counter, name, duration, duration, None))
        job_counter += 1

    while job_queue or current_job:
        # 2% chance for a new job to arrive
        if random.randint(1, 100) <= 2:
            name = f"W{job_counter}"
            priority = random.randint(1, 10)
            duration = random.randint(1, 50)
            heapq.heappush(job_queue, (-priority, current_time, job_counter, name, duration, duration, None))
            job_counter += 1

        if not current_job and job_queue:
            job = heapq.heappop(job_queue)
            # Set start_time to current_time
            current_job = (*job[:6], current_time)

        if current_job:
            # Unpack and update
            prio, arrival, job_id, name, duration, remaining, start_time = current_job
            remaining -= 1
            if remaining == 0:
                wait_time = start_time - arrival
                completed_jobs.append((name, -prio, duration, wait_time))
                current_job = None
            else:
                # Continue processing the current job
                current_job = (prio, arrival, job_id, name, duration, remaining, start_time)

        current_time += 1

    for idx, (name, priority, duration, wait_time) in enumerate(completed_jobs, start=1):
        print(f"{idx} {name} {priority} {duration} {wait_time}")

# Initial jobs (name, priority, duration)
input_data = [
    ("N", 3, 11),
    ("E", 4, 30),
    ("T", 6, 15),
    ("A", 7, 21),
    ("F", 8, 25),
    ("H", 5, 18)
]

simulate_scheduler(input_data)
