#!/usr/bin/env python3
import sys

sys.stdin.readline() #Skip column headers
for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    ip = words[0]
    date = words[1]
    #Files can only be distinct by their accesion
    #So I keep it regardless of name behind the extention
    extention=words[6].split('.')
    filename=""
    if extention[0]=="":
        filename = "" + words[5] + words[6]
    else:
        filename = words[6]
    print('%s\t%s' %( str([ip, filename]), date ) )




