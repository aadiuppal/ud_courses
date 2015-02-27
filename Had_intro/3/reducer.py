#!/usr/bin/python
import sys
import collections
count_ip=0
count_req2=0
count={}
old_request=""
this_count=0
for line in sys.stdin:
	data_mapped=line.strip().split("\t")
	if len(data_mapped)!=2:
		continue
	this_ip,this_request=data_mapped
	if old_request and this_request != old_request:
		if  old_request in count.keys():	
			count[old_request]+=this_count
		else:
			count[old_request]=this_count
		this_count=0
	old_request=this_request
	this_count+=1
	if this_request == "/assets/css/combined.css":
		count_req2+=1
	if this_ip=="10.99.99.186":
		count_ip+=1
print count_req2
print count_ip
if old_request and old_request in count.keys():
	count[old_request]+=this_count
else:
	count[old_request]=this_count
#print count
for i in  sorted(count,key=count.__getitem__):
	print "{0}\t{1}".format(i,count[i])
#print sorted(count.values())
#print len(count)
