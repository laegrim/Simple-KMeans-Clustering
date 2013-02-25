Simple-KMeans-Clustering
========================

*******************************************************
Simple attempt at a KMeans clustering algorithm in python
Written using python 2.7
Requires the random, os, and sys modules (these should be standard)

********************************************************
Input should be space seperated coordinates (I haven't tested on anything but R2, but it should work).
Outputs clustered coordinates to output.txt and error information to Log.txt

********************************************************
usage:		python kmeans.py <k> <input.txt>

********************************************************
Included script random_gen.py is a simple input file generator
Output is always in the local directory and called input.txt

usage: 		python random_gen.py <output range> <number of coordinates>

********************************************************
The included input.txt and output.txt files were generated using a range of 30000 and 15000 
coordinate pairs

