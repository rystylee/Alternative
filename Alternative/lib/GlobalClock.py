##　------------------------------------------------------------------------------

## GlobalClock.py
## GlobalCLock manages the overall performance time.

##　------------------------------------------------------------------------------


import threading
import time

from .Conductor import Conductor


class GlobalClock(threading.Timer):
    def __init__(self, bpm):
        super().__init__(interval=1/(bpm/60), function=self.run)
        self.thread = None
        self.bpm = bpm
        self.conductor = Conductor(bpm=self.bpm)


    def start(self):
        """ Main Loop """
        self.thread = threading.Timer(1/(self.bpm/60), self.start)
        self.thread.start()
        self.conductor.play(self.bpm)


    def stop(self):
        if self.thread is not None:
            self.thread.cancel()
            self.thread.join()
            del self.thread


    def set_bpm(self, bpm):
        """ Clock sleeps at interval of 1/(self.bpm/60) """
        self.bpm = bpm
