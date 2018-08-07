import threading
import time
import random


class Writer(threading.Thread):
    stop = False
    counter = 0
    queue = 0
    delay = 50

    def __init__(self, filename, r_w_mutex):
        threading.Thread.__init__(self)
        self.time = 50
        self.counter = 0
        self.r_w_mutex = r_w_mutex
        self.filename = filename

    def run(self):
        self.read()

    def read(self):
        while not Writer.stop:
            Writer.queue += 1
            with self.r_w_mutex:
                with open(self.filename, 'w') as file:
                    file.write('Writer {}: {}'.format(id(self), Writer.counter))
                Writer.counter += 1
            Writer.queue -= 1
            time.sleep(random.randrange(Writer.delay) / 1000)

    @classmethod
    def no_writer(cls):
        while True:
            if not cls.queue:
                return True

