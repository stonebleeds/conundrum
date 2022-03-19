#!/usr/bin/python

import sys, time

print "Starting script at",time.ctime()

outw=[]

ceiling=2
rejections=0
bytesread=0

try:
    while len(outw)<1024:
        b=ord(sys.stdin.read(1))
        bytesread+=1
        if b=='': raise RuntimeError, "stdin borked -- shouldn't continue"
        if b in outw[:-250]:
            rejections+=1
            continue
        outw.append(b)
        '''
        if rejections>0:
            print rejections,"rejections at",time.ctime()
            rejections=0
        '''
        if len(outw)>=ceiling:
            print "Ceiling of",ceiling,"reached at",time.ctime()
            ceiling*=2
except KeyboardInterrupt:
    print "Rejections: ",rejections,"| Bytes in outw:",len(outw),"| Bytes read:",bytesread,"|",time.ctime() 
    exit()
print "Loop done at",time.ctime()
print "[",
for h in outw: print "0x"+hex(h)[2:].upper().zfill(2)+",",
print "\b\b]"
print "Done at",time.ctime()

