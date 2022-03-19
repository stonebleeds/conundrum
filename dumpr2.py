#!/usr/bin/python

import sys, time

print "Starting script at",time.ctime()

nextbyte=sys.stdin.read(1)
while nextbyte=='': pass
print "First byte read", time.ctime()
while nextbyte!='': nextbyte=sys.stdin.read(1)
print "Last byte read. Done.",time.ctime()
