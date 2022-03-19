#!/usr/bin/python

import sys, time

cleaned=[]

time.sleep(1)

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
