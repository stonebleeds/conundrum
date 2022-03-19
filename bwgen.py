#!/usr/bin/python

import time, sys

def rd(): return ord(open("/dev/random",'rb').read(1))

print "#this part generated at",time.ctime()

tbw=[]
lastcountr=0

ceilings=[32767,49150,57341,61436,63483,64506,65017,65272,65399,65462,65493,65508,65515,65513,65533,65536]

while len(tbw)<1024:
    tbw.append(rd())

for l in ceilings:
    print "Length of tbw is",len(tbw)
    while tbw.count(tbw[-1])<(l/256.0):tbw.append(rd())
    print "Completed blind add at",time.ctime()
    while tbw.count(tbw[-1])<(len(tbw)/256.0): tbw.append(rd())
    print "Completed raw add, proceeding... |",time.ctime()
    while len(tbw)<l:
        r=rd()
        if tbw.count(r)<(len(tbw)/256.0): tbw.append(r)
        else: continue
        countr=0
        for w in range(0,256):
            if tbw.count(w)<(len(tbw)/256.0): countr+=1
        if countr!=lastcountr:
            print "Counter found to be",countr,"at",time.ctime(),'\r',
            lastcountr=countr*1
            sys.stdout.flush()
        if countr==0:
            print "Zero counter tripped at",time.ctime()
            for i in range(0,(len(tbw)/2)): tbw.append(r)
            break
    print "\n",

print tbw
