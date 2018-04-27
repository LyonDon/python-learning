#coding=utf-8
try:
	with open('cats.txt') as file_object1:
		for lines in file_object1:
			print(lines)
			pass
	with open('dogs.txt') as file_object2:
		for lines in file_object2:
			print(lines)
			pass
except IOError:
#	print('您没有此文件')
	pass
