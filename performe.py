from alternative import *

global_clock.start()
global_clock.set_interval(2.0)
global_clock.stop()

p1.set_instrument("cheappiano")
p2.set_instrument("acid_oto309")
p3.set_instrument("kick3")
p4.set_instrument("snare_stein")

p1.messages = ["cheappiano", "amp", 1.0, "freq", 540]

p1.set_original_durations([1/2])
p2.set_original_durations([1/4,1/2], [1/2])
p3.set_original_durations([1/8,1/8,1/2], [1/2,1/8])
p4.set_original_durations([1/2,1/4], [1/2, 1/2])
