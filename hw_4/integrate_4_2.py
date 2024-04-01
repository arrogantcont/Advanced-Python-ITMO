import math
import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def integrate(f, a, b, *, n_iter=10000000):
    step = (b - a) / n_iter
    acc = 0
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def parallel_integration(executor_class, func, a, b, n_jobs=1, n_iter=10000000):
    segment_size = n_iter // n_jobs
    futures = []
    with executor_class(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            segment_start = a + (b - a) * i / n_jobs
            segment_end = a + (b - a) * (i + 1) / n_jobs
            futures.append(
                executor.submit(
                    integrate, func, segment_start, segment_end, n_iter=segment_size
                )
            )

        result = sum(future.result() for future in futures)
    return result


def test_execution(f, a, b, n_iter=10000000):
    cpu_counts = ThreadPoolExecutor()._max_workers
    results = {"ThreadPoolExecutor": {}, "ProcessPoolExecutor": {}}

    for executor_class in [ThreadPoolExecutor, ProcessPoolExecutor]:
        for n_jobs in range(1, cpu_counts * 2 + 1):
            logging.info(f"Starting {executor_class.__name__} with {n_jobs} jobs")
            start_time = time.time()
            result = parallel_integration(executor_class, f, a, b, n_jobs, n_iter)
            elapsed_time = time.time() - start_time
            logging.info(
                f"Finished {executor_class.__name__} with {n_jobs} jobs: Result = {result}, Time = {elapsed_time:.2f}s"
            )
            results[executor_class.__name__][n_jobs] = elapsed_time

    return results


if __name__ == "__main__":
    logging.basicConfig(
        filename="integration_parallel_log.txt",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # Testing the execution
    a, b = 0, math.pi / 2  # Integration range
    results = test_execution(math.cos, a, b)

    # Writing results to a file
    with open("hw_4/artifacts/integration_parallel.txt", "w") as file:
        for executor, data in results.items():
            file.write(f"{executor} Results:\n")
            for n_jobs, time in data.items():
                file.write(f"  {n_jobs} jobs: {time:.2f} seconds\n")
            file.write("\n")
