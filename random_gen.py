import random

output_file = open('input.txt', 'w')
random.seed()
rand_range = range(30000)
numb_enter = range(15000)

for i in numb_enter:
	j = random.choice(rand_range)
	rand_range.pop(rand_range.index(j))
	k = random.choice(rand_range)
	rand_range.pop(rand_range.index(k))
	output_file.write(str(j) + ' ' + str(k) + '\n')
	
output_file.close()	

