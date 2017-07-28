## StopTimer
A very simple timer for Python
To simplify measuring time within code

## Installation
`pip install git+https://github.com/skjerns/stoptimer`

## Usage
```
import stimer
stimer.start()
# do stuff
stimer.stop()
# Elapsed:0.723 seconds
```
or
```
import stimer
stimer.start('Plotting')
# start some plotting
stimer.start('Calculation')
# start some calculation
stimer.stop('Calculation')
# Elapsed:0.723 seconds
# some more plotting
stimer.stop('Plotting')
# Elapsed:0.723 seconds
```
