import sys
import os

#grab command line input
if (len(sys.argv)) != 2:
	sys.exit('Usage: kmeans.py <k> <input.txt>.')

#open files
try:
	input_file = open(sys.argv[1], 'r')
	log_file = open('Log.txt', 'w')
	output_file = open('output.txt', 'w')
except IOError:
	print (IOError)
	exit()
	
x_vals = []
y_vals = []



