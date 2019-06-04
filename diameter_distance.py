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

# node.sort()
node_lenth = max(node)
print(node_lenth)

@timethis
def aaa():
	links_matrix = np.full((node_lenth, node_lenth), 1000)
	links_matrix.astype(np.int64)
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
	''' Floyd '''

	distance_matrix = np.copy(links_matrix)
	for k in range(0, node_lenth):
		for i in range(0, node_lenth):
			for j in range(0, node_lenth):
				distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k]+distance_matrix[k][j])

	print(distance_matrix.max())
aaa()
# print(distance_matrix)