#coding=utf-8
import json

try:
	numbers=int(raw_input('请输入你喜欢的数字：'))
except ValueError:
	print('请输入正确的数字')
else:
	filename='numbers.json'
	with open(filename,'w') as file_object:
		json.dump(numbers,file_object)

	filename='numbers.json'
	with open(filename) as file_object:
		json.load(file_object)

	print("I know your favorite number.It's "+str(numbers))