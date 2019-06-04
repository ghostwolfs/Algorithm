import numpy as np
import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper

# initiate network data
with open('/Users/baozi/Desktop/complex network/ARPA.txt', 'r') as f:
	line_list = f.readlines()

node = []
links = len(line_list)
for line in line_list:
	line = line.rstrip().split(' ')
	# initiate node list
	if int(line[0]) not in node:
		node.append(int(line[0]))
	if int(line[1]) not in node:
		node.append(int(line[1]))

node.sort()
node_lenth = len(node)
# print(node)
links_matrix = np.full((node_lenth, node_lenth), 0)
links_matrix.astype(np.int8)
for line in line_list:
	line = line.rstrip().split(' ')
	node_one = int(line[0]) - 1
	node_two = int(line[1]) - 1
	links_matrix[node_one][node_two] = 1
	links_matrix[node_two][node_one] = 1

for index in range(node_lenth):
	links_matrix[index][index] = 0

# print(links_matrix)
# print(links_matrix[13][15])
''' k-order matrix multiply '''
@timethis
def aaa():
	distance_matrix = np.copy(links_matrix) # C1
	k_distance_matrix = np.copy(links_matrix) # D
	temp_matrix = np.copy(links_matrix) # C2
	# print(k_distance_matrix)

	for k in range(1, node_lenth+1):
		temp_matrix = temp_matrix.dot(distance_matrix)
		current_matrix = np.zeros((node_lenth, node_lenth), dtype=np.int64)
		for i in range(0, node_lenth):
			for j in range(0, node_lenth):
				if k_distance_matrix[i][j] > 0:
					current_matrix[i][j] = k_distance_matrix[i][j]
				elif (k_distance_matrix[i][j] == 0) and (temp_matrix[i][j] > 0) and (i != j):
					current_matrix[i][j] = k+1

		# print(k_distance_matrix)
		# print(temp_matrix)
		# print(current_matrix)
		if (current_matrix == k_distance_matrix).all():
			print(k)
			break
		else:
			del k_distance_matrix
			k_distance_matrix = np.copy(current_matrix)
aaa()





