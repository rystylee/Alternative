##　------------------------------------------------------------------------------

## Conductor.py
## Conductor directs each player.

##　------------------------------------------------------------------------------


from concurrent.futures import ThreadPoolExecutor

from .Player import *


class Conductor(object):
    def __init__(self, clock_interval):
        self.clock_interval = clock_interval


    def play(self, interval):
        with ThreadPoolExecutor(max_workers=6) as executor:
            for player in players:
                executor.submit(player.play, interval)




players = []
#p1 = RhythmicPlayer(messages=["kick01"], original_durations=[[1/2,1/2],[1/4,1/2]])
#p2 = RhythmicPlayer(messages=["snare01"], original_durations=[[1/4,1/4,1/4,1/4],[1/2]])
#p1 = LSystemPlayer(messages=["kick01"], LNum_iter=5, LSeed=[1/2, 1/8], original_durations=[])
p1 = LSystemPlayer(messages=["ckick"], LNum_iter=5, LSeed=[1/2, 1/8], original_durations=[])
p2 = LSystemPlayer(messages=["snare01"], LNum_iter=5, LSeed=[1/4], original_durations=[])
#p3 = LSystemPlayer(messages=["clap01"], LNum_iter=5, LSeed=[1/8], original_durations=[])
#p4 = LSystemPlayer(messages=["hat01"], LNum_iter=4, LSeed=[1/3, 1/4], original_durations=[])
p5 = LSystemPlayer(messages=["pad01", "amp", "440"], LNum_iter=3, LSeed=[1/4, 1/8], original_durations=[])
p6 = LSystemPlayer(messages=["fmchord01"], LNum_iter=4, LSeed=[1/16], original_durations=[])
players.append(p1)
players.append(p2)
#players.append(p3)
#players.append(p4)
players.append(p5)
players.append(p6)
