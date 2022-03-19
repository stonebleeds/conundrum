#!/usr/bin/python

import sys, time, precon

print "Script started. Beginning loops at",time.ctime()

for w in range(0,256):
    for c in range(0,256):
        if precon.WHEELS[w].count(c)!=1:
            print "Found",precon.WHEELS[w].count(c),"in wheel",w,"at",time.ctime()

print "Script done."
