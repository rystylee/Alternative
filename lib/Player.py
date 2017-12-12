import time

from .OSCClient import *


class Player(object):
    def __init__(self, messages, clock_interval=1.0, duration=0.0, num_repeat=1):
        self.messages = messages
        self.duration = duration
        self.num_repeat = num_repeat
        self.clock_interval = clock_interval


    def play(self):
        """ play() means send messages to SuperCollider  """
        if self.num_repeat == 1:
            send_msg(self.messages)
        else:
            for i in range(self.num_repeat):
                send_msg(self.messages)
                if not i == (self.num_repeat - 1):
                    time.sleep(self.clock_interval / self.num_repeat)


    def set_clock_interval(self, clock_interval):
        """ to determine the sleep interval for repeat """
        self.clock_interval = clock_interval


    def set_duration(self, duration):
        self.duration = duration


    def set_num_repeat(self, num_repeat):
        self.num_repeat = num_repeat
