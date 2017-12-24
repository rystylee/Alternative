import time

from .OSCClient import *
from .Queue import Queue
from .algo.LSystem import *


class Player(object):
    def __init__(self, messages, LNum_iter, LSeed, original_durations, clock_interval=1.5):
        self.messages = messages
        self.original_durations = original_durations
        self.create_Lsystem_durations(messages="initial list", num_iters=LNum_iter, initial_list=LSeed) # Set original durations
        self.clock_interval = clock_interval

        self.num_notes = 1
        self.durations = Queue()
        self.next_durations = []


    def play(self, interval):
        self.forward_durations()
        if not self.next_durations == []:
            self.num_notes = len(self.next_durations)

            if self.num_notes == 1:
                if not self.next_durations == []:
                    time.sleep(self.next_durations[0] * interval)
                send_msg(self.messages)
            else:
                for i in range(len(self.next_durations)):
                    time.sleep(self.next_durations[i] * interval)
                    send_msg(self.messages)


    def forward_durations(self):
        if self.durations.is_Empty():
            self.durations.reset_queue(*self.original_durations)

        self.set_next_durations(self.durations.dequeue())


    def create_Lsystem_durations(self,  messages, num_iters, initial_list):
        self.original_durations = get_Lsystem(messages, num_iters, initial_list)


    def set_LSystem_durations(self, messages, num_iters, initial_list):
        self.original_durations = get_Lsystem(messages, num_iters, initial_list)


    def set_original_durations(self, *original_durations):
        self.original_durations.clear()
        for dur in original_durations:
            self.original_durations.append(dur)


    def set_durations(self, durations):
        self.durations = durations


    def set_next_durations(self, next_durations):
        self.next_durations = next_durations


    def set_instrument(self, instrument):
        self.messages[0] = instrument
