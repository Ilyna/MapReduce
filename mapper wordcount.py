#!/usr/bin/env python

import sys
import os
import re

for line in sys.stdin:
	line = line.strip()
	words = re.findall(r"[\w']+", line)
	for word in words:
		path1 = os.getenv('map_input_file')
		filename = os.path.basename(path1)	
		sys.stdout.write("{0}\t{1}\t1\n".format(word,filename))
