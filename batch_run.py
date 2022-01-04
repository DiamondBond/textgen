#!/usr/bin/env python3
import os
import sys
from datetime import datetime

# skel file

filename = sys.argv[1]
weightfile = sys.argv[2]


start_time = datetime.now()
print("Start time:", start_time)


if os.path.isfile(filename):
    if os.path.isfile(weightfile):
        try:
            string = (
                "python3 generate.py "
                + '"'
                + str(filename)
                + '"'
                + " "
                + '"'
                + str(weightfile)
                + '"'
            )

            os.system(string)

        except:
            print("error")

time_elapsed = datetime.now() - start_time
print("\nTime elapsed {}".format(time_elapsed))
