#!/usr/bin/python

import precon

print "{",

for w in range(0,256):
	print "{",
	l=0
	for n in range(0,256):
		l+=1
		print "0x"+hex(precon.WHEELS[w][n])[2:].upper().zfill(2),'\b, ',
		if l==16:
			l=0
			print ""
	print "\b\b\b},"

