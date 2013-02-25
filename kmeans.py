import sys
import os
import random

#Function: float distance(tuple, tuple)
###############################################
def distance(tuple1, tuple2):
	if (type(tuple1) != tuple or type(tuple2) != tuple):
		log_file.write("Some data might be corrupted \n")
		return 0
	if len(tuple1) == len(tuple2):
		return sum(pow(tuple1[i] - tuple2[i], 2) for i in range(len(tuple1)))
	else:
		return 0
		
###############################################

#Function: tuple mean(list[tuples])
###############################################
def mean(cluster):
	
	mean = ()
	num_axis = range(len(coord_vals[0]))
	
	for i in num_axis:
		mean = mean + ((sum(tup[i] for tup in cluster)/len(cluster)),)
			
	return mean
		 
##############################################

#grab command line input
if (len(sys.argv)) != 3:
	sys.exit('Usage: kmeans.py <k> <input.txt>.')

#open files
try:
	input_file = open(sys.argv[2], 'r')
	log_file = open('Log.txt', 'w')
	output_file = open('output.txt', 'w')
except IOError:
	print (IOError)
	exit()

#retrieve the number of means
try:
	k_means = sys.argv[1]
	k = int(k_means)
except Exception, err:
	log_file.write(str(err) + '\n')
	
#ensure the number of means is usable	
if (k < 2):
	log_file.write()
	sys.exit("Usage: number of clusters must be >= 2 \n")

coord_vals = []
clusters = [[] for i in range(k)]

#parse the file for x and y coordinates
for line in input_file:
	line = line.encode(encoding='UTF-8', errors='strict')
	data = line.split(' ')

	try:
		#put the coordinates into tupples
		coord_tuple = tuple(int(i) for i in data) 
		coord_vals.append(coord_tuple)
	except Exception, err:
		log_file.write(str(err) + '\n')
		exit()

#initialize the cluster list 
for coord_tuple in coord_vals:
	clusters[0].append(coord_tuple)

changed = 1
iteration = 0

#while clusters haven't converged to final solution
while (changed == 1):
	
	changed = 0
	means = []
	random.seed()
	#print "Means: " + str(means) + '\n'
	
	if iteration == 0:
		#while there isn't a mean for each cluster
		while (len(means) != k):
		
			#pick a random point to be an initial mean
			pick = random.choice(clusters[0])
			while (len(means) > 0 and pick == means[0]):
				pick = random.choice(clusters[0])
				
			#push pick into the mean list
			means.append(pick)
				
			#transfer the pick to a new cluster, as the mean is always in it's own cluster
			curr_cluster_index = clusters[0].index(pick)		
			tup = clusters[0].pop(curr_cluster_index)
			curr_mean_index = means.index(pick)
			clusters[curr_mean_index].append(tup)
				
			#update loop status to reflect that a coordinate changed cluster membership
			changed = 1
			#print "Transferred random starting mean " + str(pick) + " from cluster 0 " + \
			#" to cluster " + str(len(means) - 1) + '\n'
			
	elif iteration > 0:
		for cluster in clusters:
			means.append(mean(cluster))
	
	for cluster in clusters:
	
		for coord in cluster:
			
			#the mean of the same index of the cluster is the mean of the cluster
			mean_index = clusters.index(cluster)
			closest_mean = means[mean_index]
			
			for i in range(len(means)):
				
				#if the distance is shorter to another mean than the mean of the cluster then
				if (distance(coord, means[i]) < distance(coord, closest_mean)):
					closest_mean = distance(coord, means[i])
					mean_index = i
			
			if closest_mean != means[clusters.index(cluster)]:
				#transfer the current coordinate from it's cluster to the cluster with the closer mean
				clusters[means.index(means[mean_index])].append(cluster.pop(cluster.index(coord)))
				#update loop status to reflect that a coordinate changed cluster membership
				changed = 1
				#print "Transferred point " + str(coord) + " from cluster " + str(clusters.index(cluster)) + \
				#" to cluster " + str(means.index(means[mean_index])) + '\n'
	
	#print "Changed: " + str(changed) + '\n'
	#print "Iteration: " + str(iteration) + '\n'
	#print "Means: " + str(means) + '\n'
	#print "Clusters: " + str(clusters) + '\n'
	iteration = iteration + 1
				
for cluster in clusters:
	for coords in cluster:
		for axis in coords:		
			output_file.write(str(axis) + ' ')
			
		output_file.write(str(clusters.index(cluster)) + '\n')
	
	
input_file.close()
log_file.close()
output_file.close()
		
	

			



