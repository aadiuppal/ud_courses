#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

#########################################################
### your code goes here ###
from sklearn import svm
#c=[10,100,1000,10000,100000]
c=[10000]
count=0
for i in c:
	clf=svm.SVC(C=i,kernel="rbf")
	t0=time()
	clf.fit(features_train,labels_train)
	print "training time:", round(time()-t0, 3), "s"
	t1=time()
	pred=clf.predict(features_test)
	print "training time:", round(time()-t1, 3), "s"
	from sklearn.metrics import accuracy_score
	accuracy = accuracy_score(labels_test,pred)
	print "for C=",i,"  accuracy=",accuracy
	print "for 10",pred[10]
	print "for 26",pred[26]
	print "for 50",pred[50]
	for i in pred:
		if i==1:
			count+=1
	print count
#########################################################


