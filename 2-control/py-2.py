from threading import Thread, RLock
import logging
from time import time, sleep

lock = RLock()


def func(locker, delay):
    timer = time()
    with locker:
        sleep(delay)
    logging.debug(f'Done {time() - timer}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    t1 = Thread(target=func, args=(lock, 2))
    t2 = Thread(target=func, args=(lock, 2))
    t1.start()
    t2.start()
    logging.debug('Started')

"""
MainThread Started
Thread-1 Done 2.0014190673828125
Thread-2 Done 4.002039194107056
"""