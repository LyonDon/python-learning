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
'''
message=input("please input a number")
num=int(message)

while num<=20:
	print(num)
	pass
'''

#三明治列表
sandwish_orders=['a','s','cs','pastrami','pastrami','pastrami']
print('pastrami has been sold out')
print(sandwish_orders)

while 'pastrami' in sandwish_orders:
		sandwish_orders.remove('pastrami')
		pass
finished_sandwiches=[]

for sandwish in sandwish_orders:
	print(sandwish+' I made your tuna sandwish')
	finished_sandwiches.append(sandwish)
	pass

print(finished_sandwiches)

#用户输入填充字典,若是使用列表则只需一个输入值
holiday_palces={}

while True:
	question=input('\nwhere do you want to go:')
	holiday_palce=input('\n')
	holiday_palces[question]=holiday_palce

	repeat=raw_input('\ndoes anyone want to have a test?')
	if repeat=='No':
		break
		pass
	else:
		continue

print('result----------')
print(holiday_palces)