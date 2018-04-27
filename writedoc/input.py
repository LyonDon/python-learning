#coding=utf-8
name=raw_input('请输入你的名字：')

file_name='guest.txt'
with open('guest.txt','a') as file_object:
	file_object.write(name)
