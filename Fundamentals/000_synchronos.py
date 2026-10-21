#Synchronous programming executes task sequentially

import time 

def task_a():
    print("Task A started..")
    time.sleep(3)
    print("Task A finished...")

def task_b():
    print("Task B started..")
    time.sleep(2)
    print("Task B completed...")

def main():
    start_time = time.perf_counter()

    task_a()
    task_b()

    end_time = time.perf_counter()

    total_time = end_time - start_time

    print(f"Total time taken {total_time : .2f} seconds ") 


main()