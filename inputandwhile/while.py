#coding=utf-8
message="\n请输入一种披萨配料:"
message+="\n输入quit退出"

while True:
	s=raw_input(message)
	if s=='quit':
		break
		pass
	else:
		print("we will add "+s)
	pass
	break

#电影院问题
message="\n请输入您的年龄"

while True:
	age=raw_input(message)
	age=int(age)
	if age<3:
		print('free')
	elif age<12:
		print('10dollars')
	else:
		print('15dollars')
		pass
	pass
	break

#无限循环
#编辑器崩了
message=input("please input a number")
num=int(message)

while num<=20:
	print(num)
	pass