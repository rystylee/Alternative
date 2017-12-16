import time

from .OSCClient import *
from .Queue import Queue


class Player(object):
    def __init__(self, messages, clock_interval=1.0):
        self.messages = messages
        self.clock_interval = clock_interval
        self.num_notes = 1
        self.durations = Queue()
        self.next_durations = []


    def play(self, interval):
        if self.next_durations == []:
            self.num_notes = 1
        else:
            self.num_notes = len(self.next_durations)

        if self.num_notes == 1:
            if not self.next_durations == []:
                time.sleep(self.next_durations[0])
            send_msg(self.messages)
        else:
            for i in range(len(self.next_durations)):
                time.sleep(self.next_durations[i])
                print(self.next_durations[i])
                send_msg(self.messages)


    def set_durations(self, durations):
        self.durations = durations


    def set_next_durations(self, next_durations):
        self.next_durations = next_durations
