## ------------------------------------------------------------------------------

## player.py
## Player means a performer.

## ------------------------------------------------------------------------------


import time
import random

from .osc_client import *
from .util.queue import Queue
from .algo.l_system import *


class Player(object):
    def __init__(self, messages, original_durations):
        # An OSC messges to send to SuperCollider
        self._messages = messages

        # Original duration is the default dutation's list
        self._original_durations = original_durations

        # durations is like [[1/3, 1/2, 1/8], [1/4,1/4], .. ]
        # next_durations is like [1/3, 1/2, 1/8]
        self._durations = Queue()
        self._next_durations = []

        # Stopping flag
        self._is_running = True

        # The higher the density, the higher the performance frequency
        self._density = 0.4

        # The first element of the messages means each player's instruent
        self._instrument = self._messages[0]

        # Player plays as many as num_note in one cycle
        self._num_notes = 1


    def play(self, bpm):
        if not self._is_running:
            print("{} is paused.".format(self._instrument))
        else:
            print("{0}'s density is {1}".format(self._instrument, self._density))
            if random.random() < self._density:
                self.forward_durations()
                self.set_freq(random.randint(200, 3000))

                if not self._next_durations == []:
                    self._num_notes = len(self._next_durations)
                    if self._num_notes == 1:
                        time.sleep(self._next_durations[0] * 1/(bpm/60))
                        send_msg(self._messages)
                    else:
                        for i in range(len(self._next_durations)):
                            time.sleep(self._next_durations[i] * 1/(bpm/60))
                            send_msg(self._messages)
                else:
                    print("{}'s next_durations is empty".format(self._instrument))


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
        """ Take out next_durations one by one from durations """

        if self._durations.is_Empty():
            self._durations.reset_queue(*self._original_durations)

        self._next_durations = self._durations.dequeue()
        print("{0}'s next_durations : {1}".format(self._instrument, self._next_durations))


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
    """ RhythmicPlayer plays regularly """
    def __init__(self, messages, original_durations):
        super().__init__(messages, original_durations)



class LSystemPlayer(Player):
    """ LSystemPlayer creates durations using L-system and plays accordingly """
    def __init__(self, messages, LNum_iter, LSeed, original_durations):
        super().__init__(messages, original_durations)
        self.create_Lsystem_durations(messages="initial list", num_iters=LNum_iter, initial_list=LSeed) # Set original durations


    def create_Lsystem_durations(self,  messages, num_iters, initial_list):
        self._original_durations = get_Lsystem(messages, num_iters, initial_list)


    def set_LSystem_durations(self, messages, num_iters, initial_list):
        self._original_durations = get_Lsystem(messages, num_iters, initial_list)
