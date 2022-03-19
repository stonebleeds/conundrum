#!/usr/bin/python

cr=[]

print "Starting generating loop"

while len(cr)<256:
	r=ord(open("/dev/random",'rb').read(1))
	if r in cr: pass
	else: cr.append(r)

m=[]

print "Starting check loop"

for i in range(0,256):
	if not cr.count(i)==1: raise RuntimeError, "found "+str(cr.count(i))+" "+str(i)+" YOU DONE GOOFED"
	if i in cr: pass
	else: m.append(i)

print '" ": [',
for c in cr: print "0x"+hex(c)[2:].upper().zfill(2)+",",
print "\b\b],"

