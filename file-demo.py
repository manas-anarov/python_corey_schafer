# f = open('test.txt', 'r')

# print(f.name)
# f.close()


# f = open('test.txt', 'r')

# print(f.mode)
# f.close()



# with open('test.txt', 'r') as f:
# 	pass

# print(f.closed)



# with open('test.txt', 'r') as f:
# 	f_contents = f.read()

# 	print(f_contents)

# with open('test.txt', 'r') as f:
# 	f_contents = f.readline()

# 	print(f_contents)



# with open('test.txt', 'r') as f:
# 	f_contents = f.readline()
# 	print(f_contents, end='')

# 	f_contents = f.readline()
# 	print(f_contents, end='')



# # from __future__ import print_function
# with open('test.txt', 'r') as f:
# 	for line in f:
# 		print(line, end='')


# 	# f_contents = f.readline()
# 	# print(f_contents, end='')

# 	# f_contents = f.readline()
# 	# print(f_contents, end='')




# with open('test.txt', 'r') as f:
# 	f_contents = f.read()
# 	print(f_contents, end='')


# with open('test.txt', 'r') as f:
# 	f_contents = f.read(100)
# 	print(f_contents, end='')

# 	f_contents = f.read(100)
# 	print(f_contents, end='')

# 	f_contents = f.read(100)
# 	print(f_contents, end='')


# with open('test.txt', 'r') as f:
# 	size_to_read = 100

# 	f_contents = f.read(size_to_read)
# 	while len(f_contents) > 0:
# 		print(f_contents, end='')
# 		f_contents = f.read(size_to_read)


# with open('test.txt', 'r') as f:
# 	size_to_read = 10

# 	f_contents = f.read(size_to_read)
# 	while len(f_contents) > 0:
# 		print(f_contents, end='*')
# 		f_contents = f.read(size_to_read)

# with open('test.txt', 'r') as f:
# 	size_to_read = 10

# 	f_contents = f.read(size_to_read)

# 	print(f.tell())

# 	# while len(f_contents) > 0:
# 	# 	print(f_contents, end='*')
# 	# 	f_contents = f.read(size_to_read)


# with open('test.txt', 'r') as f:
# 	size_to_read = 10

# 	f_contents = f.read(size_to_read)
# 	print(f_contents, end='')

# 	f.seek(0)

# 	f_contents = f.read(size_to_read)
# 	print(f_contents)



# with open('test2.txt', 'w') as f:
# 	f.write('Test')
# 	f.seek(0)
# 	f.write('rest22')


# with open('test2.txt', 'w') as f:
# 	f.write('Test')
# 	f.seek(0)
# 	f.write('rest22')


# with open('index.jpeg', 'rb') as rf:
# 	with open('index_copy.jpeg', 'wb') as wf:
# 		for line in rf:
# 			wf.write(line)


with open('index.jpeg', 'rb') as rf:
	with open('index_copy.jpeg', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)