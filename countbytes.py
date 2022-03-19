#!/usr/bin/python

import sys,time

print "Countbytes started at",time.ctime()

thresh=1
bytedict={}
for i in range(0,256): bytedict[chr(i)]=0

time.sleep(3)

print "Intake loop starting at",time.ctime()

nextbyte=sys.stdin.read(1)
while nextbyte=='':
	time.sleep(1)
	nextbyte=sys.stdin.read(1)

while nextbyte:
	bytedict[nextbyte]+=1
	if bytedict[nextbyte]>=thresh:
		print "Threshold of",thresh,"found with byte",hex(ord(nextbyte))[2:].zfill(2).upper(),"at",time.ctime()
		thresh=thresh<<1
	nextbyte=sys.stdin.read(1)

print "Loop done at",time.ctime()

for i in range(0,256):
	print hex(i)[2:].zfill(2).upper(),bytedict[chr(i)]

print "Countbytes done at",time.ctime()
