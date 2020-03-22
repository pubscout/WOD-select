#!/usr/bin/env python

import random


file = open("WODS.txt")

wods = [line.rstrip('\n') for line in file.readlines() if line.strip()]

wod = random.choice(wods)

print "Today's WOD: ", wod
