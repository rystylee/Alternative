import time
from .OSCClient import *


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
