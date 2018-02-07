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
        self._thread = None
        self._bpm = bpm
        self._conductor = Conductor(bpm=self._bpm)


    def start(self):
        """ Main Loop """
        self._thread = threading.Timer(1/(self._bpm/60), self.start)
        self._thread.start()
        self._conductor.play(self._bpm)


    def stop(self):
        if self._thread is not None:
            self._thread.cancel()
            self._thread.join()
            del self._thread


    @property
    def bpm(self):
        """ Clock sleeps at interval of 1/(self._bpm/60) """
        return self._bpm


    @bpm.setter
    def bpm(self, bpm):
        self._bpm = bpm