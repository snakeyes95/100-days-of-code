import threading
import time

thread_list=[]


def thread_info(thread_number):
    print(f'Starting Thread {thread_number}')
    time.sleep(2)
    print(f'Ending Thread {thread_number}')


if __name__ == '__main__':
#creating multiple threads
    for thread_number in range(4):
        thread_obj=threading.Thread(target=thread_info,args=(thread_number,))
        thread_list.append(thread_obj)
        thread_obj.start()

#joining threads
    for thread_number,thread_obj in enumerate(thread_list):
        print(f'joining thread {thread_number}')
        thread_obj.join()
        print(f'joining {thread_number} completed!')

