import multiprocessing
import time

# ------------------ Functions ------------------
def func1(sec: int):
    '''
    Simulates a task that takes `sec` seconds to complete.

    Args:
        sec (int): Number of seconds to sleep (simulate work).
    '''
    print(f"[func1] Sleeping for {sec} seconds...")
    time.sleep(sec)
    print(f"[func1] Finished after {sec} seconds.")


def func2(sec: int):
    '''
    Another simulated task that takes `sec` seconds to complete.

    Args:
        sec (int): Number of seconds to sleep (simulate work).
    '''
    print(f"[func2] Sleeping for {sec} seconds...")
    time.sleep(sec)
    print(f"[func2] Finished after {sec} seconds.")


if __name__ == "__main__":
    # ------------------ Sequential Execution ------------------
    print("Running sequentially...\n")
    start_time = time.perf_counter()

    func1(5)
    func1(4)
    func1(2)

    end_time = time.perf_counter()
    print(f"\nTime Taken (sequential): {end_time - start_time:.2f} seconds")

    # ------------------ Parallel Execution with Multiprocessing ------------------
    print("\nRunning with multiprocessing...\n")
    start_time = time.perf_counter()

    # Create process objects for each function call
    p1 = multiprocessing.Process(target=func1, args=(5,))
    p2 = multiprocessing.Process(target=func1, args=(4,))
    p3 = multiprocessing.Process(target=func1, args=(2,))

    # Start all processes
    p1.start()
    p2.start()
    p3.start()

    # Wait for all processes to complete
    p1.join()
    p2.join()
    p3.join()

    end_time = time.perf_counter()
    print(f"\nTime Taken (multiprocessing): {end_time - start_time:.2f} seconds")
