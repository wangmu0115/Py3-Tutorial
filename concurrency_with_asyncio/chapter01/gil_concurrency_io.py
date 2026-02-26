import time
from threading import Thread

import httpx


def read_example():
    resp = httpx.get("http://www.example.com")
    print(f"{resp.status_code}")


# start = time.perf_counter()
# read_example()
# read_example()
# end = time.perf_counter()
# print(f"Running synchronously took {end - start:.4f} seconds.")

start = time.perf_counter()
thread1 = Thread(target=read_example, args=())
thread2 = Thread(target=read_example, args=())
thread1.start()
thread2.start()
print("All threads started.")
thread1.join()
thread2.join()
end = time.perf_counter()
print(f"Running with threads took {end - start:.4f} seconds.")
