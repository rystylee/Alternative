from .Player import Player

class Conductor:
    def __init__(self):
        print("Conductor")


    def play():
        for player in players:
            player.play()

        # p1.play()
        # p2.play()
        # p3.play()
        # p4.play()


players = []
p1 = Player(messages=["kick01", "amp", 1.0, "decay", 0.5], interval=0.2)
p2 = Player(messages=["snare01", "amp", 1.0, "decay", 0.5], interval=0.2)
p3 = Player(messages=["clap01", "amp", 1.0], interval=0.2)
p4 = Player(messages=["piano01"], interval=0.2)
players.append(p1)
players.append(p2)
players.append(p3)
players.append(p4)
