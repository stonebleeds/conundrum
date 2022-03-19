#!/usr/bin/python

import time, sys

triggers=['\x00','\n','\b']

time.sleep(3)

r=sys.stdin.read(1)

while r:
	print hex(ord(r))[2:].upper().zfill(2),
	if r in triggers: sys.stdout.flush()
	r=sys.stdin.read(1)

