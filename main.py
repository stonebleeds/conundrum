#!/usr/bin/python2.7

# setting 0x0123 0x4567
# wheel 0x01, position 0x23 with position 0x4567 on bigwheel
#  -or-
# setting 0x89AB 0xCDEF 0x3030
# wheels 0x89 and 0xCD, with positions 0xAB and 0xEF respectively,
# with position 0x3030 on bigwheel


# because I don't want to write the code to handle for otherwise right
# now, each instance of conundrum (for the time being) must have
# one wheel w/ position AND a position on the bigwheel
# (I do want to EVENTUALLY write code that will handle just ONE 16-bit
# number, and that will mean a position on the bigwheel)


import precon, sys, time, os

version="0.03ab"
sleepintervalmax = 5

flushline=0
outcount=0
lastflush=time.time()
flushlinelimit=40

diagnosticlines=[]

def diagwriteout():
    global diagnosticlines, outcount
    #flname=str(int(time.time()))+"diag.txt"
    flname="diag"+str(int(time.time()))
    for i in sys.argv[1:]:flname=flname+"_"+i
    while "0x" in flname: flname=flname.replace("0x",'')
    if len(flname)>240: flname=flname[:240]+"V"
    flname=flname+".txt"
    while os.path.exists(flname):
        diagnosticlines.append(time.ctime()+" No joke, "+flname+" seems to exist. Waiting...\r\n")
        time.sleep(0.9)
        flname="diag"+str(int(time.time()))
        for i in sys.argv[1:]:flname=flname+"_"+i
        if len(flname)>240: flname=flname[:240]+"V"
        flname=flname+".txt"
    diagnosticlines.append("Final count appears to be "+str(outcount)+" / "+hex(outcount)+"\r\n")
    diagnosticlines.append(time.ctime()+" Writing diagnostics to "+flname+"\r\n")    
    open(flname,'wb').writelines(diagnosticlines)

work=sys.argv[1:]
bigwheelpos=int(work.pop(-1)[2:],16)

diagnosticlines.append("Started conundrum "+version+" with precon.py version "+precon.PRECONVER+" and options:\r\n")
for i in sys.argv: diagnosticlines.append(i+' ')
diagnosticlines.append("\r\nat "+time.ctime()+"\r\n")
diagnosticlines.append("Work list shows up as "+str(work)+" <---\r\n")
diagnosticlines.append("bigwheelpos appears to be "+hex(bigwheelpos)+"\r\n")

cassette=[]
#wheelpos=0x0
wheelposstr=""
cassettelength=len(work)

diagnosticlines.append("cassette length is figured to be "+str(cassettelength)+" / "+hex(cassettelength)+"\r\n")

while work:
    workl=work.pop(0)
    diagnosticlines.append("workl appears to be "+workl+"\r\n")
    setting=workl[2:].zfill(4)
    wheelstr=setting[:2]
    posstr=setting[2:]
    diagnosticlines.append("adding setting "+setting+" with wheel "+wheelstr+" at position "+posstr+"\r\n")
    cassette.append(precon.WHEELS[int(wheelstr,16)])
    wheelposstr=wheelposstr+posstr
    diagnosticlines.append("wheelposstr appears to be "+wheelposstr+"\r\n")

wheelpos=int(wheelposstr,16)

diagnosticlines.append("preliminary wheelpos is "+hex(wheelpos)+"\r\n")

'''
while work:
    wheelpos=wheelpos<<8
    workl = work.pop(0)
    diagnosticlines.append("workl appears to be "+workl+"\r\n")
    setting=workl[2:].zfill(4)
    wheel=int(setting[:2],16)
    position=int(setting[2:],16)
    diagnosticlines.append("adding setting "+setting+" with wheel "+hex(wheel)+" at position "+hex(position)+"\r\n")
    cassette.append(precon.WHEELS[wheel])
    wheelpos+=position
    diagnosticlines.append("wheelpos is now at "+hex(wheelpos)+"\r\n")
    if wheelpos==0:
        diagnosticlines.append("First wheel position cannot be zero in this version. I'd apologize, but whatever.\r\n")
        diagwriteout()
        raise RuntimeError, "unsupported wheel position"
'''

diagnosticlines.append("Moving on...\r\n")
wheelposmask=(256**cassettelength)-1
diagnosticlines.append("wheelposmask is figured to be "+hex(wheelposmask)+"\r\n")

wheelpos=wheelpos&wheelposmask

diagnosticlines.append("wheelpos is figured to be "+hex(wheelpos)+"\r\n")

diagnosticlines.append("starting intake loops at "+time.ctime()+"\r\n")

# these two lines (and the following loop, for that matter) are there because
# some processes don't start sending data through the pipe in a timely fashion
# this is sometimes referred to as the "delay timer"
sleepinterval=0
time.sleep(sleepinterval)

nextbyte=sys.stdin.read(1)
while nextbyte=="": # this is the "delay timer"
    sleepinterval+=1
    if sleepinterval >= sleepintervalmax:
        diagnosticlines.append(time.ctime()+" Sleep interval exceeded set maximum of "+str(sleepintervalmax)+" seconds before processing loops. Calling it.")
        diagwriteout()
        raise RuntimeError, "Never got incoming bytes and hit interval limit."
    diagnosticlines.append(time.ctime()+" nextbyte empty before processing loops. Sleep interval currently at "+str(sleepinterval)+".\r\n")
    time.sleep(sleepinterval)
    diagnosticlines.append(time.ctime()+" Trying again...\r\n")
    nextbyte=sys.stdin.read(1)

while nextbyte!='':
    if wheelpos==0: diagnosticlines.append(time.ctime()+" Wheel positions are at 0\r\n")
    xr = 0
    positionbytes=hex(wheelpos)[2:].zfill(2*cassettelength)
    if positionbytes[-1]=='L':
        positionbytes=positionbytes[:-1].zfill(2*cassettelength)
    positionbytelist=[positionbytes[j:j+2].zfill(2) for j in range(0, len(positionbytes), 2)]
    if positionbytelist[-1]=='L':
        waste=positionbytelist.pop(-1)
    for x in range(0,cassettelength):
        try: xr = xr ^ cassette[x][int(positionbytelist[x],16)]
        except ValueError:
            diagnosticlines.append("Choked at xr calculation with a ValueError at "+time.ctime()+'\r\n')
            diagnosticlines.append("positionbytelist looks like:\r\n")
            diagnosticlines.append(str(positionbytelist)+"\r\n")
            diagwriteout()
            raise RuntimeError, "choked and wrote out"
    xr = xr ^ precon.BW[bigwheelpos]
    sys.stdout.write(chr(ord(nextbyte)^xr))
    outcount+=1
    flushline+=1
    if flushline>flushlinelimit:
        try:
            sys.stdout.flush()
            # trying to have this just be code that has the script flushing stdout at a consistent pace -- I am probably failing at this
            if time.time()-lastflush < 3: flushlinelimit+=1
            if time.time()-lastflush > 4: flushlinelimit-=1
            lastflush=time.time()
        except IOError:
            diagnosticlines.append("Choked on an IOError while trying to flush the stdout with positionbytelist looking like:\r\n")
            diagnosticlines.append(str(positionbytelist)+"\r\n")
            diagnosticlines.append("bigwheelpos looks like:"+hex(bigwheelpos)+"\r\n")
            diagnosticlines.append("Might be a case of unrecommended stacking...\r\n")
            diagwriteout()
            raise RuntimeError, "choked and wrote out"
        flushline=0
        #spot check
    if hex(outcount)[-5:]=='18680':
        diagnosticlines.append("Spot check triggered at "+time.ctime()+"\r\n")
        diagnosticlines.append("positionbytelist looks like:\r\n")
        diagnosticlines.append(str(positionbytelist)+"\r\n")
        diagnosticlines.append("bigwheelpos looks like:"+hex(bigwheelpos)+"\r\n")
    wheelpos+=1
    wheelpos=wheelpos&wheelposmask
    bigwheelpos+=1
    bigwheelpos=bigwheelpos&0xffff
    #if not bigwheelpos: diagnosticlines.append("bigwheel position appears to be zero at "+time.ctime()+"\r\n")
    nextbyte=sys.stdin.read(1)

diagnosticlines.append(time.ctime()+" Intake loops appear to be done.\r\n")
diagnosticlines.append(time.ctime()+" Wheel positions are "+hex(wheelpos)+"\r\n")

#might remove this part later -- reporting final positions and xrs
positionbytes=hex(wheelpos)[2:].zfill(2*cassettelength)
if positionbytes[-1]=='L':
    positionbytes=positionbytes[:-1].zfill(2*cassettelength)
diagnosticlines.append("positionbytes appears to be "+positionbytes+"\r\n")
positionbytelist=[positionbytes[j:j+2].zfill(2) for j in range(0, len(positionbytes), 2)]
#positionbytelist=[positionbytes[j:j+2] for j in range(0, len(positionbytes), 2)]
diagnosticlines.append("positionbytelist looks like "+str(positionbytelist)+"\r\n")
lxr=0
diagnosticlines.append("xrs appear to be:\r\n")
for x in range(0,cassettelength):
    lxr = lxr ^ cassette[x][int(positionbytelist[x],16)]
    diagnosticlines.append(hex(lxr)+" ")
diagnosticlines.append(" <----\r\n")
diagnosticlines.append("bigwheel at position "+hex(bigwheelpos)+" is "+hex(precon.BW[bigwheelpos])+"\r\n")
diagnosticlines.append("last xr was "+hex(xr)+"\r\n")

diagnosticlines.append(time.ctime()+" Done.\r\n")

diagwriteout()
