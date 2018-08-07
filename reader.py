import threading
import time
from writer import Writer


class Reader(threading.Thread):
    stop = False
    n = 3
    sem = threading.Semaphore(n)

    def __init__(self, filename, r_w_mutex):
        threading.Thread.__init__(self)
        self.filename = filename
        self.r_w_mutex = r_w_mutex

    def run(self):
        self.read()

    def read(self):
        while not Reader.stop:
            with Reader.sem:
                with self.r_w_mutex:
                    self.r_w_mutex.wait_for(Writer.no_writer)
                    with open(self.filename, 'r+') as file:
                        print('Reader {}: \n\t{}'.format(id(self), file.read()))
            time.sleep(2)
