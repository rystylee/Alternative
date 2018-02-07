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
    def __init__(self, messages, original_durations):
        self._messages = messages
        self._original_durations = original_durations

        self._is_running = True
        self._density = 0.4
        self._instrument = self._messages[0]

        self._num_notes = 1
        self._durations = Queue()
        self._next_durations = []


    def play(self, bpm):
        if not self._is_running:
            print("{} is paused.".format(self._instrument))
        else:
            print("{0} 's density is {1}.".format(self._instrument, self._density))
            if random.random() < self._density:
                self.forward_durations()
                self.set_freq(random.randint(200, 3000))

                if not self._next_durations == []:
                    self._num_notes = len(self._next_durations)

                    if self._num_notes == 1:
                        if not self._next_durations == []:
                            time.sleep(self._next_durations[0] * 1/(bpm/60))
                        send_msg(self._messages)
                    else:
                        for i in range(len(self._next_durations)):
                            time.sleep(self._next_durations[i] * 1/(bpm/60))
                            send_msg(self._messages)


    def pause(self):
        if self._is_running:
            self._is_running = False
        else:
            print("{} is already paused.".format(self._instrument))


    def restart(self):
        if not self._is_running:
            self._is_running = True
        else:
            print("{} is already started.".format(self._instrument))


    def increase_density(self):
        self._density += 0.1


    def decrease_density(self):
        self._density -= 0.1


    def forward_durations(self):
        if self._durations.is_Empty():
            self._durations.reset_queue(*self._original_durations)

        # self.set_next_durations(self._durations.dequeue())
        self._next_durations = self._durations.dequeue()
        print("{} : ".format(self._instrument), self._next_durations)


    def set_original_durations(self, *original_durations):
        self._original_durations.clear()
        for dur in original_durations:
            self._original_durations.append(dur)


    def set_freq(self, freq):
        self._messages = [self._instrument, "freq", freq]


    @property
    def durations(self):
        return self._durations


    @durations.setter
    def durations(self, durations):
        self._durations = durations


    @property
    def next_durations(self):
        return self._next_durations


    @next_durations.setter
    def next_durations(self, next_durations):
        self._next_durations = next_durations


    @property
    def instrument(self):
        return self._instrument


    @instrument.setter
    def instrument(self, instrument):
        self._instrument = instrument



class RhythmicPlayer(Player):
    def __init__(self, messages, original_durations):
        super().__init__(messages, original_durations)



class LSystemPlayer(Player):
    def __init__(self, messages, LNum_iter, LSeed, original_durations):
        super().__init__(messages, original_durations)
        self.create_Lsystem_durations(messages="initial list", num_iters=LNum_iter, initial_list=LSeed) # Set original durations


    def create_Lsystem_durations(self,  messages, num_iters, initial_list):
        self._original_durations = get_Lsystem(messages, num_iters, initial_list)


    def set_LSystem_durations(self, messages, num_iters, initial_list):
        self._original_durations = get_Lsystem(messages, num_iters, initial_list)
