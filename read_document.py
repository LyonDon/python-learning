with open('learning-python.txt') as file_object:
	'''
	contents=file_object.read()
	print(contents)
	'''
	for line in file_object:
		l=line.replace('python','C')
		print(l.rstrip())
#		print(line)
		pass

	'''
	lines=file_object.readlines()
for line in lines:
	line.replace('python','C')
	pass
	
with open('learning-python.txt') as file_object:
	print(file_object.read())
	'''
#	contents=file_object.read()
#	print(contents)