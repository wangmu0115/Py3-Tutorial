import os
import threading
import time

print(f"Python process running with process id: {os.getpid()}.")
total_threads = threading.active_count()
curr_thread_name = threading.current_thread().name
print(f"Python is currently running {total_threads} thread(s).")
print(f"The current thread is {curr_thread_name}.")


def hello_from_thread():
    print(f"Hello from thread: {threading.current_thread()}")
    time.sleep(1)


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

print(f"Python is currently running {threading.active_count()} thread(s).")
print(f"The current thread is {threading.current_thread().name}.")

hello_thread.join()
