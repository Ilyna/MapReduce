#!/usr/bin/env python

from operator import itemgetter
import sys

currentauthor = None
currentterm = None
author = None
total = 0

for line in sys.stdin:
    line = line.strip()
    author, term, count = line.split('\t')
    term = str(term)   
    count = int(count)
	
    if currentauthor == author:
	if lastterm == term:
		total += count
	else:
		currentterm = currentterm+': '+str(total)+', '+term
		lastterm=term
		total=1
		total=int(total)
    else:
        if currentauthor:
            print '%s\t%s: %i' % (currentauthor, currentterm, total)

	lastterm=term
        currentterm = term
        currentauthor = author
	total = 1
	total = int(total)
if currentauthor == author:
    print '%s\t%s: %i' % (currentauthor, currentterm, total)

