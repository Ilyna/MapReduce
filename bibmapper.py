#!/usr/bin/env python

import sys

stopwords = open('/home/training/Documents/stopwords','r').read().split()

for line in sys.stdin:
	line = line.strip()
	words = line.split('::')

	paper = words[0]
	title = words[-1]
	title = title.translate(None, ':()-.,<>;"!?/=+*[`]')
	authors = words[1:-1]
	
	for author in authors:
		author = author.translate(None, ':')
		terms=title.split()
		for term in terms:
			if term.lower() not in stopwords:		
				sys.stdout.write("{0}\t{1}\t1\n".format(author,term))
