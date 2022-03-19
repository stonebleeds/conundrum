#!/usr/bin/python

import sys, time

print "detecttwo.py started at",time.ctime()

count=0

lastbyte=sys.stdin.read(1)

print "Counting loop starting at",time.ctime()

while lastbyte!='':
	nextbyte=sys.stdin.read(1)
	if lastbyte==nextbyte: print "Found byte","0x"+hex(ord(nextbyte))[2:].upper().zfill(2),"near count","0x"+hex(count).upper()[2:],"at",time.ctime()
	count+=1
	lastbyte=nextbyte

print "Counting loop finished at",time.ctime()
print count,"bytes read."
