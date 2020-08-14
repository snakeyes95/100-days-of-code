import threading
import time

total=0

def list_sum(*args):
    global total
    for i in args:    
        total=i+total
        if i%2 == 0:
            time.sleep(2)
        print(total)
    print(f'Total is {total}')



if __name__ == '__main__':
    thread1= threading.Thread(target=list_sum,args=[1,2,3,4,5])
    thread1.start()
    thread1.join()
    thread2= threading.Thread(target=list_sum,args=[10,10,10,10])
    thread2.start()
    print('Main ends here !')
