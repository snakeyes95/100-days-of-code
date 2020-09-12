from multiprocessing import Process
import os 

def find_square(val):
    print(os.getppid())
    print(os.getpid())
    print(val*val)


if __name__ == '__main__':
    p=Process(target=find_square,args=(12,))
    p.start()
    p.join()
