#!/usr/bin/python
# main.py (wheel positions in hex) wheels... bigwheelpos
# ./main.py 0x000b2e1affff 39 164 41 157 60 226 0x0123

import precon, sys, time, os

version="0.01nu"

flushline=0

diagnosticlines=[]

diagnosticlines.append("Started precon "+version+" with options:\r\n")
for i in sys.argv: diagnosticlines.append(i+' ')

diagnosticlines.append("\r\nat "+time.ctime()+"\r\n")

w1=precon.WHEELS[int(sys.argv[2])]# 40 bits shifted
w2=precon.WHEELS[int(sys.argv[3])]# 32 bits shifted
w3=precon.WHEELS[int(sys.argv[4])]# 24 bits shifted
w4=precon.WHEELS[int(sys.argv[5])]# 16 bits shifted
w5=precon.WHEELS[int(sys.argv[6])]# 8 bits shifted
w6=precon.WHEELS[int(sys.argv[7])]# 0 bits shifted

bigwheelpos=int(sys.argv[8][2:],16)

diagnosticlines.append(time.ctime()+" Defined stuff, doing whlpos loop\r\n")

whlpos=int(sys.argv[1][2:],16)

#time.sleep(3)

nextbyte=sys.stdin.read(1)
while nextbyte=='':
	time.sleep(3)
	nextbyte=sys.stdin.read(1)
	diagnosticlines.append(time.ctime()+" Triggering empty next byte...\r\n")

while nextbyte!='':
	if whlpos==0: diagnosticlines.append(time.ctime()+" Wheel positions are at 0\r\n")
	xr=w1[(whlpos>>40)&0xff]^w2[(whlpos>>32)&0xff]^w3[(whlpos>>24)&0xff]^w4[(whlpos>>16)&0xff]^w5[(whlpos>>16)&0xff]^w6[whlpos&0xff]^precon.BW[bigwheelpos]
	sys.stdout.write(chr(ord(nextbyte)^xr))
	flushline+=1
	if flushline>40:
                sys.stdout.flush()
                flushline=0
	whlpos+=1
	whlpos=whlpos&0xffffffffffff
	bigwheelpos+=1
	bigwheelpos=bigwheelpos&0xffff
	nextbyte=sys.stdin.read(1)

diagnosticlines.append(time.ctime()+" Wheel positions are 0x"+hex(whlpos)[2:].upper().zfill(12)+'\r\n')
diagnosticlines.append(time.ctime()+" Done.\r\n")
flname=str(int(time.time()))+"diag.txt"
while os.path.exists(flname):
	time.sleep(0.9)
	flname=str(int(time.time()))+"diag.txt"
open(flname,'wb').writelines(diagnosticlines)
