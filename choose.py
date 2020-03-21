#!/usr/bin/env python

import random

#wods = open("WODS.txt").readlines()
wods = [line.rstrip('\n') for line in open("WODS.txt")]

wod = random.choice(wods)

print "Today's WOD: ", wod
