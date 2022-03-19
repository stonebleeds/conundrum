#!/usr/bin/python
#binhexoutlabel.py label

import time, sys

triggers=['\x00','\n','\b']

time.sleep(3)

print "Stream labeled",sys.argv[1],"started at",time.ctime()

r=sys.stdin.read(1)

while r:
	print hex(ord(r))[2:].upper().zfill(2),
	if r in triggers: sys.stdout.flush()
	r=sys.stdin.read(1)

sys.stdout.write("\r\n")
print "Script done at",time.ctime()
