##　------------------------------------------------------------------------------

## Conductor.py
## Conductor directs each player.

##　------------------------------------------------------------------------------


from concurrent.futures import ThreadPoolExecutor

from .Player import Player


class Conductor(object):
    def __init__(self, clock_interval):
        self.clock_interval = clock_interval


    def play(self, interval):
        with ThreadPoolExecutor(max_workers=6) as executor:
            for player in players:
                executor.submit(player.play, interval)




players = []
# p1 = Player(messages=["cheappiano", "amp", 1.0], LNum_iter=5, LSeed=[1/4], original_durations=[])
# p2 = Player(messages=["acid_oto309", "amp", 1.0], LNum_iter=5, LSeed=[1/8], original_durations=[])
# p3 = Player(messages=["kick3", "amp", 1.0], LNum_iter=5, LSeed=[1/2], original_durations=[])
# p4 = Player(messages=["snare_stein", "amp", 0.8], LNum_iter=5, LSeed=[1/3], original_durations=[])
# players.append(p1)
# players.append(p2)
# players.append(p3)
# players.append(p4)
# p1 = Player(messages=["ab_009_ab2ride"], LNum_iter=5, LSeed=[1/4], original_durations=[])
# p2 = Player(messages=["ab_002_ab2hit1"], LNum_iter=5, LSeed=[1/8], original_durations=[])
# p3 = Player(messages=["ab_003_ab2hit2"], LNum_iter=5, LSeed=[1/2], original_durations=[])
# p4 = Player(messages=["ab_010_ab2snare1"], LNum_iter=5, LSeed=[1/3], original_durations=[])
# players.append(p1)
# players.append(p2)
# players.append(p3)
# players.append(p4)
p1 = Player(messages=["kick01"], LNum_iter=6, LSeed=[1/4], original_durations=[])
p2 = Player(messages=["clap01"], LNum_iter=5, LSeed=[1/8], original_durations=[])
p3 = Player(messages=["snare01"], LNum_iter=6, LSeed=[1/2], original_durations=[])
p4 = Player(messages=["hat01"], LNum_iter=4, LSeed=[1/3, 1/4], original_durations=[])
p5 = Player(messages=["pad01"], LNum_iter=3, LSeed=[1/4, 1/8], original_durations=[])
p6 = Player(messages=["fmchord01"], LNum_iter=4, LSeed=[1/16], original_durations=[])
players.append(p1)
players.append(p2)
players.append(p3)
players.append(p4)
players.append(p5)
players.append(p6)
