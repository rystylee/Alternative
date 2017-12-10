import time
import threading
from .OSCClient import *

class Conductor:
    def __init__(self):
        print("Conductor")


    def play():
        p1.play()
        p2.play()
        p3.play()
        p4.play()


class Player:
    def __init__(self, messages, interval):
        self.interval = interval
        self.messages = messages


    def play(self):
        time.sleep(self.interval)
        print("bang")
        send_msg(self.messages)


    def set_interval(self, interval):
        self.interval = interval


p1 = Player(messages=["kick01", "amp", 1.0, "decay", 0.5], interval=0.2)
p2 = Player(messages=["snare01", "amp", 1.0, "decay", 0.5], interval=0.2)
p3 = Player(messages=["clap01", "amp", 1.0], interval=0.2)
p4 = Player(messages=["piano01"], interval=0.2)
