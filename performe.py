from alternative import *

global_clock.start()

global_clock.set_interval(1.0)

global_clock.stop()

p1.set_original_durations([])
p2.set_original_durations([])
p3.set_original_durations([])
p4.set_original_durations([])

p1.set_original_durations([1/2,1/4,1/4], [1/4], [1/8,1/8,1/4,1/4])
p2.set_original_durations([1/4,1/2], [1/2], [1/2,1/4,1/4])
p2.set_original_durations([1/4,1/2], [1/2])
p2.set_original_durations([1/4,1/2])
p3.set_original_durations([1/2], [1/2], [1/4,1/4,1/4])
p4.set_original_durations([1/2,1/4], [1/2, 1/2])
