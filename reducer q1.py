#!/usr/bin/env python

from operator import itemgetter
import sys

currentword = None
currentfile = None
filename = None
word = None
lastfile = None
total = 0

for line in sys.stdin:
    line = line.strip()
    word, filename, count = line.split('\t')
    filename = str(filename)   
    count = int(count)

    if currentword == word:
	if lastfile == filename:
		total += count
		continue
	else:	
		currentfile = currentfile+': '+str(total)+', '+filename + ': '
		lastfile = filename
		total = 1
		total = int(total)

    else:
        if currentword:
            print '%s\t%s %i' % (currentword, currentfile, total)

	lastfile = filename
        currentfile = filename
        currentword = word
	total = 1
	total = int(total)
if currentword == word:
    print '%s\t%s %i' % (currentword, currentfile, total)

