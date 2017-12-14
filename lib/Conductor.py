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
p1 = Player(messages=["kick01", "amp", 1.0, "decay", 0.5])
p2 = Player(messages=["snare01", "amp", 1.0, "decay", 0.5])
p3 = Player(messages=["clap01", "amp", 1.0])
p4 = Player(messages=["hat01"])
players.append(p1)
players.append(p2)
players.append(p3)
players.append(p4)
