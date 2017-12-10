import threading
import time

from .Conductor import Conductor


class GlobalClock:
    def __init__(self, interval):
        self.stop_event = threading.Event()
        self.inc_event = threading.Event()
        
        self.interval = interval
        self.thread = threading.Thread(target = self.run)


    def start(self):
        self.thread.start()


    def run(self):
        while not self.stop_event.is_set():
            time.sleep(self.interval)
            print("bang")
            Conductor.play()
            if self.inc_event.is_set():
                self.inc_event.clear()


    def stop(self):
        self.stop_event.set()
        self.thread.join()


    def set_interval(self, interval):
        self.interval = interval
