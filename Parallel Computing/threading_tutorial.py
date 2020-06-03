import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print("Sleeping {0} seconds...".format(seconds))
    time.sleep(seconds)
    print("Done Sleeping...")


thread_list = []
for _ in range(1, 10):
    t = threading.Thread(target = do_something, args = [1.5])
    t.start()
    thread_list.append(t)

for i in range(0, 9):
    thread_list[i].join()


finish = time.perf_counter()

print("Finished in: ", round(finish - start, 2))
