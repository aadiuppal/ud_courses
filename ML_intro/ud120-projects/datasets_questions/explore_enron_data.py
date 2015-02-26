#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
print len(enron_data["SKILLING JEFFREY K"])
count=0
for ii in enron_data:
	for i in enron_data[ii]:
		if i == "poi":
			if enron_data[ii]["poi"] == 1:
				count+=1
print count

file = open("../final_project/poi_names.txt","r")
file.readline()
file.readline()
line=0
for ii in file:
	line+=1
print line
for i in enron_data:
	l=i.split(" ")
	if l[0]=="SKILLING":
		print i
print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print "total_payemnts fastow - lay- skilling"
print enron_data["FASTOW ANDREW S"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["SKILLING JEFFREY K"]["total_payments"]
count_mail=0
count_salary=0
count_tot_pay=0
count_tot_pay_poi=0
print enron_data["SKILLING JEFFREY K"]
for ii in enron_data:
	for i in enron_data[ii]:
		if i=="salary" and enron_data[ii][i]!="NaN":
			count_salary+=1
		if i=="email_address" and enron_data[ii][i] != "NaN":
			count_mail+=1
		if i=="total_payments" and enron_data[ii][i] != "NaN":
			count_tot_pay+=1
	if enron_data[ii]["poi"]== "NaN" and enron_data[ii]["total_payments"]=="NaN":
		count_tot_pay_poi+=1
print count_salary
print count_mail
print "NaN total payments",len(enron_data)-count_tot_pay
print 1-(float(count_tot_pay)/len(enron_data))
print 1-(float(count_tot_pay)/(len(enron_data)+len(enron_data["SKILLING JEFFREY K"])))
print count_tot_pay_poi
print 1-(float(count_tot_pay_poi)/count)
