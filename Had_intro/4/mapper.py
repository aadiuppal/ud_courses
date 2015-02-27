#!/usr/bin/python
import sys
import re
for line in sys.stdin:
	data=line.strip().split('.| |,|!|?|:|;|\"|(|)|<|>|[|]|#|$|=|-|/|?')
	print data
	print len(data)
