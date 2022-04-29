#!/usr/bin/env python3

from operator import itemgetter
import sys

lastIp = None
lastFilename = None
lastDate = None
lastPrinted = ["", ""] #Keep last printed pair to evade duplicate results

for input in sys.stdin:
    input = input.strip('')
    input = input.split('\t')
    #Get the key values [ip, filename]
    key = input[0].strip('[]').split(',')
    ip = key[0]
    filename = key[1]

    #Get date from value
    date = input[1]

    #Lines 23 and 24 could merge but would get too big
    #Also the logical flow makes more sence
    #Because the input is sorted by key same keys will be together
    #For each key check if there are at least 2 values for date
    #If the key hasnt been printed before, print it
    if lastIp==ip and lastFilename==filename and not lastDate==date:
        if not(lastPrinted[0]==ip and lastPrinted[1]==filename):
            print('%s\t%s' %(lastIp, lastFilename) )
            lastPrinted = [lastIp, lastFilename]
    lastIp = ip
    lastDate = date
    lastFilename = filename
