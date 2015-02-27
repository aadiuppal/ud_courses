#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
salesMax=0
tot_sales=0
num_sales=0
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    num_sales+=1
    tot_sales+=float(thisSale)
    if oldKey and oldKey != thisKey:
        print oldKey, "\t",salesMax# salesTotal
        oldKey = thisKey;
        salesMax=0
	salesTotal = 0

    oldKey = thisKey
    if salesMax < float(thisSale):
	salesMax=float(thisSale)
    salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesMax#salesTotal
print "Total Sales",tot_sales,"   Num sales",num_sales
