from threading import Semaphore, Thread
import logging
from time import sleep


def worker(condition):
    with condition:
        logging.debug(f'Got semaphore')
        sleep(1)
        logging.debug(f'finished')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    pool = Semaphore(2)
    for num in range(10):
        thread = Thread(name=f'Th-{num}', target=worker, args=(pool, ))
        thread.start()

"""
Th-0 Got semaphore
Th-1 Got semaphore
Th-1 finished
Th-0 finished
Th-2 Got semaphore
Th-3 Got semaphore
Th-3 finished
Th-2 finished
Th-4 Got semaphore
Th-5 Got semaphore
Th-5 finished
Th-4 finished
Th-6 Got semaphore
Th-7 Got semaphore
Th-7 finished
Th-6 finished
Th-8 Got semaphore
Th-9 Got semaphore
Th-9 finished
Th-8 finished
"""