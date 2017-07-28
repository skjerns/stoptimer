## StopTimer
A very simple timer for Python
To simplify measuring time within code

## Installation
`pip install git+https://github.com/skjerns/StopTimer`

## Usage
```Python
import stimer
stimer.start()
stimer.sleep(1) # do calculations
stimer.stop()
# Elapsed:1.000 seconds
```
or
```Python
import stimer
stimer.start('Plotting')
# start some plotting
stimer.sleep(0.2)
stimer.start('Calculation')
# start some calculation
stimer.sleep(0.3)
stimer.stop('Calculation')
# Elapsed:0.723 seconds
# some more plotting
stimer.sleep(0.2)
stimer.stop('Plotting')
# Elapsed:0.723 seconds
```