##　------------------------------------------------------------------------------

## Player.py
## Player means a performer.

##　------------------------------------------------------------------------------


import time
import random

from .OSCClient import *
from .Queue import Queue
from .algo.LSystem import *


class Player(object):
    def __init__(self, messages, original_durations, clock_interval=1.0):
        self.messages = messages
        self.instrument = self.messages[0]
        self.original_durations = original_durations
        self.clock_interval = clock_interval
        self.is_running = True

        self.num_notes = 1
        self.durations = Queue()
        self.next_durations = []


    def play(self, interval):
        if not self.is_running:
            print("{} is paused.".format(self.instrument))

        else:
            if random.random() < 0.4:
                self.forward_durations()
                self.set_freq(random.randint(200, 3000))

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



    def set_freq(self, freq):
        self.messages = [self.instrument, "freq", freq]


    def forward_durations(self):
        if self.durations.is_Empty():
            self.durations.reset_queue(*self.original_durations)

        self.set_next_durations(self.durations.dequeue())
        print("{} : ".format(self.instrument), self.next_durations)


    def set_original_durations(self, *original_durations):
        self.original_durations.clear()
        for dur in original_durations:
            self.original_durations.append(dur)


    def set_durations(self, durations):
        self.durations = durations


    def set_next_durations(self, next_durations):
        self.next_durations = next_durations


    def set_instrument(self, instrument):
        self.instrument = instrument


    def pause(self):
        if self.is_running:
            self.is_running = False
        else:
            print("{} is already paused.".format(self.instrument))

    def restart(self):
        if not self.is_running:
            self.is_running = True
        else:
            print("{} is already started.".format(self.instrument))



class RhythmicPlayer(Player):
    def __init__(self, messages, original_durations, clock_interval=1.0):
        super().__init__(messages, original_durations, clock_interval)



class LSystemPlayer(Player):
    def __init__(self, messages, LNum_iter, LSeed, original_durations, clock_interval=1.0):
        super().__init__(messages, original_durations, clock_interval)

        self.create_Lsystem_durations(messages="initial list", num_iters=LNum_iter, initial_list=LSeed) # Set original durations


    def create_Lsystem_durations(self,  messages, num_iters, initial_list):
        self.original_durations = get_Lsystem(messages, num_iters, initial_list)


    def set_LSystem_durations(self, messages, num_iters, initial_list):
        self.original_durations = get_Lsystem(messages, num_iters, initial_list)
