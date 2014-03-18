#!/usr/bin/env python


# chmod +x mean_sightings.py # will make the file as an executable which can be run by ./mean_sightings.py
# also add python in the path
import sys
import pandas as pd
import numpy as np
def get_sightings(filename, focusanimal):
    """
    Returns the total No of sightings and the mean No of animal seen per
    sighting in a file
    
    filename, focusanimal should both be strings.
    This will return 0, 0 if the animal is not present
    """
    # Load table
    tab = pd.read_csv(filename)
    # Standardize capitalization of focusanimal
    focusanimal = focusanimal.capitalize()
    # Loop through all records, countings recs and animals
    totalrecs = 0.0
    totalcount = 0
    for i, rec in tab.iterrows(): # Iterate through DataFrame rows
        if rec['Animal'] == focusanimal:
            totalrecs += 1
            totalcount += rec['Count']
	if totalcount == 0:
            meancount = 0.0
        else:
		meancount = totalcount/totalrecs
    # Return num of records and animals seen
    return totalrecs, meancount

if __name__ == '__main__': # without this, the script can only be called in command-line
    # allows for giving input from command line - this is like a command now
	filename = sys.argv[1]
	focusanimal = sys.argv[2]
	print 'The NO and mean of ' + focusanimal + ' is %d, %0.1f' % get_sightings(filename, focusanimal)
