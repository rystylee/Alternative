##　------------------------------------------------------------------------------

## performe.py
## Performance starts.

##　------------------------------------------------------------------------------


from Alternative import *

global_clock.start()
global_clock.set_interval(4.5)
global_clock.stop()

p1.set_instrument("cheappiano")
p2.set_instrument("PMCrotale")
p3.set_instrument("kick3")
p4.set_instrument("snare_stein")

p1.set_original_durations([1/2])
p2.set_original_durations([1/4,1/2], [1/2])
p3.set_original_durations([1/8,1/8,1/2], [1/2,1/8])
p4.set_original_durations([1/2,1/4], [1/2, 1/2])
