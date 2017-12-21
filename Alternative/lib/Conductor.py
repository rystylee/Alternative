from concurrent.futures import ThreadPoolExecutor

from .Player import Player


class Conductor(object):
    def __init__(self, clock_interval):
        self.clock_interval = clock_interval


    def play(self, interval):
        with ThreadPoolExecutor(max_workers=4) as executor:
            for player in players:
                executor.submit(player.play, interval)




players = []
p1 = Player(messages=["cheappiano", "amp", 1.0], LNum_iter=5, LSeed=[1/4], original_durations=[])
p2 = Player(messages=["acid_oto309", "amp", 1.0], LNum_iter=5, LSeed=[1/8], original_durations=[])
p3 = Player(messages=["kick3", "amp", 1.0], LNum_iter=5, LSeed=[1/2], original_durations=[])
p4 = Player(messages=["snare_stein", "amp", 0.8], LNum_iter=5, LSeed=[1/3], original_durations=[])
players.append(p1)
players.append(p2)
players.append(p3)
players.append(p4)
