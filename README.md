# Alternative
a Python library for LiveCoding.


## Description
Alternative is a LiveCoding library implemented by Python. Alternative controls the rhythm and actual sound generation is done by OSC communication with SuperCollider.


## Demo
![result](https://github.com/rystylee/Alternative/blob/master/demo.gif)


## Dependence
* python-osc


## Usage
First of all run synthdefs.scd on SuperCollider. 
Below is an example to execute a .scd file on the command line (it is necessary to pass through the path of sclang):
```shell
sclang synthdefs.scd
```
You can use synthdefs which you defined by yourself.

Import Alternative:
```Python
from Alternative import *
```

Then, when you start global_clock, you hear a sound:
```Python
global_clock.start()
```

If you want to change bpm, execute the following method:
```Python
global_clock.set_bpm(120)
```

for more information, see example.
