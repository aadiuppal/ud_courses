#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    import numpy as np
    cleaned_data = []
    error=[]
    #predictions=np.array(predictions)
    #ages=np.array(ages)
    #net_worths=np.array(net_worths)
    ### your code goes here
    for i in range(0,len(predictions)):
    	error.append(abs(predictions[i]-net_worths[i]))#**2)
    count=0.1*len(predictions)

    #print error
    """    error=np.array(error)
    while count>0:
	#print ages[error.index(max(error))]
	#print error.index(max(error))
	#ages= ages[:(error.index(max(error)))]+ages[(error.index(max(error)))+1:]
	#net_worths= net_worths[:(error.index(max(error)))]+net_worths[(error.index(max(error)))+1:]
	#error= error[:(error.index(max(error)))]+error[(error.index(max(error)))+1:]
	ages=np.delete(ages,np.array(np.where(error==max(error))).tolist())#error.index(max(error)))
	net_worths=np.delete(net_worths,np.array(np.where(error==max(error))).tolist())#error.index(max(error)))
	error=np.delete(error,np.array(np.where(error==max(error))).tolist())#error.index(max(error)))
	count=count-1
    for i in range(0,len(ages)):
	cleaned_data.append((ages[i],net_worths[i],error[i]))
    """
    cleaned_data = zip(ages, net_worths, error)

    ###sort the unclean clean data by error
    cleaned_data.sort(key=lambda tup: tup[2])
	
    #delete the last 10 entries which have the greatest error
    cleaned_data = cleaned_data[:81]
    return cleaned_data

