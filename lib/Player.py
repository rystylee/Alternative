import time

from .OSCClient import *


class Player(object):
    def __init__(self, messages, clock_interval=1.0):
        self.messages = messages
        self.clock_interval = clock_interval
        self.num_notes = 1
        self.durations = []

    def play(self, interval):
        print(interval)
        """ play() means sending messages to SuperCollider  """
        if self.durations == []:
            self.num_notes = 1
        else:
            self.num_notes = len(self.durations)

        if self.num_notes == 1:
            if not self.durations == []:
                time.sleep(self.durations[0])
            send_msg(self.messages)
        else:
            for i in range(len(self.durations)):
                time.sleep(self.durations[i])
                print(self.durations[i])
                send_msg(self.messages)


    def set_clock_interval(self, clock_interval):
        """ to determine the sleep interval for repeat """
        self.clock_interval = clock_interval


    def set_durations(self, durations):
        self.durations = durations
