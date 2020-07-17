import time
from threading import Thread
import random

choices=['rock','paper','scissors']


def task(i):
    choice=random.choice(choices)
    print(f'thread {i} selected {choice}')
    

for i in range(4):
    t = Thread(target=task, args=(i,))
    t.start()