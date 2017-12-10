import time

from .OSCClient import *

class Player(object):
    def __init__(self, messages, clock_interval=1.0, duration=0.0, num_repeat=1):
        self.messages = messages
        self.duration = duration
        self.num_repeat = num_repeat
        self.clock_interval = clock_interval


    def play(self):
        for i in range(self.num_repeat):
            if not self.num_repeat == 1 and not i == 0:
                time.sleep(self.clock_interval / self.num_repeat)

            send_msg(self.messages)


    def set_clock_interval(self, clock_interval):
        self.clock_interval = clock_interval


    def set_duration(self, duration):
        self.duration = duration


    def set_num_repeat(self, num_repeat):
        self.num_repeat = num_repeat
