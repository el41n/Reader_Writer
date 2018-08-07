import threading
import signal
from reader import Reader
from writer import Writer


def main():
    def stop(sig, frame):
        for reader in readers:
            Reader.stop = True
            Writer.stop = True

    signal.signal(signal.SIGINT, stop)

    N = 10
    M = 2
    r_w_mutex = threading.Condition()
    filename = 'shared_file'
    readers = [Reader(filename, r_w_mutex) for i in range(N)]
    writers = [Writer(filename, r_w_mutex) for i in range(M)]

    for writer in writers:
        writer.start()

    for reader in readers:
        reader.start()

    signal.pause()


if __name__ == '__main__':
    main()
