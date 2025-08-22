import threading
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


    # ------------------ Parallel Execution with Threads ------------------
    print("\nRunning with threads...\n")
    start_time = time.perf_counter()

    # Create thread objects for each function call
    t1 = threading.Thread(target=func1, args=(5,))
    t2 = threading.Thread(target=func1, args=(4,))
    t3 = threading.Thread(target=func1, args=(2,))

    # Start all threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for all threads to complete
    t1.join()
    t2.join()
    t3.join()

    end_time = time.perf_counter()
    print(f"\nTime Taken (multithreading): {end_time - start_time:.2f} seconds")
