#!/usr/bin/python

for n in range(8,256):
	print n,": [",
	g=[]
	while len(g)<256:
		b=ord(open("/dev/random",'rb').read(1))
		if b in g: continue
		else: g.append(b)
	for i in g: print "0x"+hex(i)[2:].upper().zfill(2)+",",
	print "\b\b],"
