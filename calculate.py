# Got started by reading https://github.com/pytroll/pyorbital/issues/22

from pyorbital import tlefile
from pyorbital.orbital import Orbital
from datetime import datetime
import argparse

# altitude (km) above seal-level and lat lon of the observer
TLE_FILE_NAME = 'cubesat.txt'
ALTITUDE_ASL = 0
LAT = 64.146
LONG = 21.942


passhour = 0

while passhour < 24:
    # set the date with a variable for the hour
    d = datetime(2020, 5, 9, passhour, 0, 0)
    orb = Orbital('CUBESAT', 'cubesat.txt')
    # generate pass information for the hour specified
    passes = orb.get_next_passes(d, 1, LONG, LAT, ALTITUDE_ASL, horizon=1)
    # if there is no pass for the current value of passhour, the length will be zero
    if len(passes) > 0:
        rise_az, rise_el = orb.get_observer_look(passes[0][0], LONG, LAT, ALTITUDE_ASL)
        transit_az, transit_el = orb.get_observer_look(passes[0][2], LONG, LAT, ALTITUDE_ASL)
        set_az, set_el = orb.get_observer_look(passes[0][1], LONG, LAT, ALTITUDE_ASL)

        # print out the pass info
        print("CUBESAT")
        print(passes[0][0], rise_az, rise_el)
        print(passes[0][2], transit_az, transit_el)
        print(passes[0][1], set_az, set_el)
        print()
        # use datetime.strptime() to split the pass time into its componenet parts
        # set the hour of the current pass
        passtring = datetime.strptime(str(passes[0][0]), '%Y-%m-%d %H:%M:%S.%f')
        passhour = passtring.hour
        # iterate to the next hour
        passhour += 1

    else:
        # iterate to the next hour
        passhour += 1


