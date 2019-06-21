"""
Example programme that runs on a Pycom board and prints plantower readings.
Daniel Hausner
20/06/2019
"""

from plantower import Plantower, PlantowerException

plantower = Plantower()

while True:
    try:
        recv = plantower.read()
        print(recv)
    except PlantowerException as pe:
        print(pe)