#!/usr/bin/python

import sys, time

count=0
order=10

alertcounts=[6,66,666,6666,42069]
for i in range(3,63): alertcounts.append(2**i)

nextbyte=sys.stdin.read(1)
while nextbyte=='':
    print "Waiting for first byte. <--",time.ctime()
    time.sleep(1.01)
    nextbyte=sys.stdin.read(1)

while nextbyte!='':
    count+=1
    if order==count:
        count*=10
        print "Order increased at",time.ctime()
    if count in alertcounts: print "ALERT",count,"<--",time.ctime()
    nextbyte=sys.stdin.read(1)

print "nextbyte failed at",time.ctime()
print "Done."
