import random
import sys

#grab command line input
if (len(sys.argv)) != 3:
	sys.exit('Usage: random_gen.py <output range> <number of coordinates>')

output_file = open('input.txt', 'w')
random.seed()
rand_range = range(int(sys.argv[1]))
numb_enter = range(int(sys.argv[2]))

for i in numb_enter:
	j = random.choice(rand_range)
	rand_range.pop(rand_range.index(j))
	k = random.choice(rand_range)
	rand_range.pop(rand_range.index(k))
	output_file.write(str(j) + ' ' + str(k) + '\n')
	
output_file.close()	

