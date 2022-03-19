#!/usr/bin/python

import time, sys

print "Script started, libraries imported, starting 3-second wait"

time.sleep(3)

print "Wait over"

b=sys.stdin.read(1)

print "first byte read,",hex(ord(b)),"starting loop"

while b!='\x00':
	b=sys.stdin.read(1)
	print hex(ord(b)),"!",

print "Done"
