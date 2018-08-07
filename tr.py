import threading
import time
import logging
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

q = 0

def f():
    while True:
        #print('checked', q)
        sys.stdout.flush()
        if not q:
            return True


def consumer(cv):
    while True:
        logging.debug('Consumer thread started ...')
        with cv:
            logging.debug('Consumer waiting ...')
            condition.wait_for(f)
            logging.debug('Consumer consumed the resource')
        time.sleep(2)

def producer(cv):
    while True:
        global q
        q += 1
        logging.debug('Producer thread started ...')
        with cv:
            logging.debug('Making resource available')
            logging.debug('Notifying to all consumers')
            #cv.notifyAll()
        q -= 1
        time.sleep(10)


if __name__ == '__main__':
    condition = threading.Condition()
    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))
    pd = threading.Thread(name='producer', target=producer, args=(condition,))
    pd2 = threading.Thread(name='producer2', target=producer, args=(condition,))

    pd.start()
    cs1.start()
    cs2.start()
    pd2.start()
    cs1.join()

