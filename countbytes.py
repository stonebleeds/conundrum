#!/usr/bin/python2.7

import sys,time

print "Countbytes started at",time.ctime()

thresh=1
bytedict={}
finalcount=0
for i in range(0,256): bytedict[chr(i)]=0

time.sleep(3)

print "detecting input... ",time.ctime()

nextbyte=sys.stdin.read(1)
while nextbyte=='':
	print "still no input..."
	time.sleep(1)
	nextbyte=sys.stdin.read(1)

print "Intake loop starting at",time.ctime()

while nextbyte:
	bytedict[nextbyte]+=1
	if bytedict[nextbyte]>=thresh:
		print "Threshold of",thresh,"found with byte",hex(ord(nextbyte))[2:].zfill(2).upper(),"at",time.ctime()
		thresh=thresh<<1
	nextbyte=sys.stdin.read(1)

print "Loop done at",time.ctime()

for i in range(0,256):
	print '0x'+hex(i)[2:].zfill(2).upper()+'\t'+str(bytedict[chr(i)])

for i in range(0,256):
	finalcount+=bytedict[chr(i)]
print finalcount,"bytes counted"

highest=('',0)
for i in range(0,256):
	cchr,ccnt=highest
	if ccnt<bytedict[chr(i)]: highest=chr(i),bytedict[chr(i)]

cchr,ccnt=highest
print "most occurred is probably",hex(ord(cchr)),"with",ccnt,"times"

lowest='',ccnt
for i in range(0,256):
	cchr,ccnt=lowest
	if ccnt>bytedict[chr(i)]: lowest=chr(i),bytedict[chr(i)]

print "least occurred is probably",hex(ord(cchr)),"with",ccnt,"times"

print "Countbytes done at",time.ctime()
