import threading
import time

from .Conductor import Conductor


class GlobalClock(threading.Timer):
    def __init__(self, interval=1.0):
        super().__init__(interval=interval, function=self.run)
        self.thread = None
        self.interval = interval
        self.conductor = Conductor(self.interval)


    def start(self):
        """ Main Loop """
        self.thread = threading.Timer(self.interval, self.start)
        self.thread.start()
        self.conductor.set_clock_interval(self.interval)
        self.conductor.play()


    def stop(self):
        if self.thread is not None:
            self.thread.cancel()
            self.thread.join()
            del self.thread


    def set_interval(self, interval):
        """ Clock sleeps at interval of self.interval """
        self.interval = interval
