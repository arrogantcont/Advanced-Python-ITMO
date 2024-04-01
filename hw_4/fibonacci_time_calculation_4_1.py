import time
import threading
import multiprocessing


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def synchronous_fibonacci(n, times):
    start_time = time.time()
    for _ in range(times):
        fibonacci(n)
    return time.time() - start_time


def threading_fibonacci(n, times):
    threads = []
    start_time = time.time()
    for _ in range(times):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return time.time() - start_time


def multiprocessing_fibonacci(n, times):
    processes = []
    start_time = time.time()
    for _ in range(times):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    return time.time() - start_time


def average_time(func, n, times, repeat=10):
    total_time = 0
    for _ in range(repeat):
        total_time += func(n, times)
    return total_time / repeat


def compare_time(n, times, repeat=10):
    sync_time = average_time(synchronous_fibonacci, n, times, repeat)
    thread_time = average_time(threading_fibonacci, n, times, repeat)
    process_time = average_time(multiprocessing_fibonacci, n, times, repeat)

    results = (
        f"Synchronous: {round(sync_time, 4)} s\n"
        f"Threading: {round(thread_time, 4)} s\n"
        f"Multiprocessing: {round(process_time, 4)} s"
    )

    print(results)
    with open("time_compare.txt", "w") as file:
        file.write(results)


if __name__ == "__main__":
    n = 25
    t = 10
    compare_time(n, t)
