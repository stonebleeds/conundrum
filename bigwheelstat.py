#!/usr/bin/python

import precon,sys,time

print "Starting bigwheelstat at",time.ctime()

print "Length appears to be",len(precon.BW)

for i in range(0,256):
	print '\b'+str(i).zfill(3),"\t",precon.BW.count(i),'\t',"\b|",
	if i%6==5: print ""

print ""
print "Done at",time.ctime()
