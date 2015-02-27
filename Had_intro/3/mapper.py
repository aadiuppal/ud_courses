#!/usr/bin/python
import sys
str="http://www.the-associates.co.uk"
str1="http://the-associates.co.uk"

for line in sys.stdin:
	data=line.strip().split(" ")
	if len(data)==10:
		ip,id,user,time,time_zone,request1,request2,request3,status,bytes=data
		if request2[:len(str)]==str:
			request2=request2[len(str):]
		if request2[:len(str1)]==str1:
			request2=request2[len(str1):]
		print "{0}\t{1}".format(ip,request2)
