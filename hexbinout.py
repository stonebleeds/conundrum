#!/usr/bin/python

import sys, time

cleaned=[]

print "Script started at",time.ctime()

time.sleep(4)

print "Initial wait done at",time.time()

f=sys.stdin.read(10)

while f!='':
	f=f.replace(" ",'')
	while len(f)>1:
		cleaned.append(f[:2])
		f=f[2:]
	while cleaned: sys.stdout.write(chr(int(cleaned.pop(0),16)))
	sys.stdout.flush()
	f=f+sys.stdin.read(10)

while cleaned: sys.stdout.write(chr(int(cleaned.pop(0),16)))
