"""
Example programme that runs on a Pycom board and prints plantower readings.
Daniel Hausner
20/06/2019
"""

from Plantower import Plantower

plantower = Plantower()

while True:
    recv = plantower.read()
    print(recv)