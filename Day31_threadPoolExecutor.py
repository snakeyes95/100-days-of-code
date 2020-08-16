import threading
import time
import concurrent.futures

def thread_info(thread_number):
    print(f'Starting Thread {thread_number}')
    time.sleep(2)
    print(f'Ending Thread {thread_number}')




with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_info,range(3))
